<?php

namespace App\Http\Controllers;

use App\Models\Course;
use Illuminate\Support\Str;
use Illuminate\Http\Request;
use App\Http\Requests\CourseRequest;

class CourseController extends Controller
{
    // =========================
    // 📚 Danh sách + Search + Sort
    // =========================
    public function index(Request $request)
    {
        $query = Course::with(['lessons', 'enrollments'])
            ->withCount(['lessons', 'students']);

        // 🔍 Tìm theo tên
        $query->when($request->name, function ($q) use ($request) {
            $q->where('name', 'like', '%' . $request->name . '%');
        });

        // 💰 Giá <=
        $query->when($request->price, function ($q) use ($request) {
            $q->where('price', '<=', $request->price);
        });

        // 📌 Trạng thái
        $query->when($request->status, function ($q) use ($request) {
            $q->where('status', $request->status);
        });

        // 🔥 Sắp xếp
        $query->when($request->sort, function ($q) use ($request) {

            if ($request->sort == 'price_asc') {
                $q->orderBy('price', 'asc');
            }

            if ($request->sort == 'price_desc') {
                $q->orderBy('price', 'desc');
            }

            if ($request->sort == 'students') {
                $q->orderBy('students_count', 'desc');
            }

            if ($request->sort == 'newest') {
                $q->orderBy('created_at', 'desc');
            }
        });

        $courses = $query->paginate(5)->appends($request->all());

        return view('courses.index', compact('courses'));
    }

    // =========================
    // ➕ Form thêm
    // =========================
    public function create()
    {
        return view('courses.create');
    }

    // =========================
    // 💾 Lưu
    // =========================
    public function store(CourseRequest $request)
    {
        $data = $request->validated();

        // 🔥 Tạo slug không trùng
        $slug = Str::slug($data['name']);
        $originalSlug = $slug;
        $count = 1;

        while (Course::withTrashed()->where('slug', $slug)->exists()) {
            $slug = $originalSlug . '-' . $count;
            $count++;
        }

        $data['slug'] = $slug;

        // upload ảnh
        if ($request->hasFile('image')) {
            $data['image'] = $request->file('image')->store('courses', 'public');
        }

        Course::create($data);

        return redirect()->route('courses.index')->with('success', 'Thêm thành công');
    }

    // =========================
    // ✏️ Form sửa
    // =========================
    public function edit($id)
    {
        $course = Course::findOrFail($id);
        return view('courses.edit', compact('course'));
    }

    // =========================
    // 🔄 Update
    // =========================
    public function update(CourseRequest $request, $id)
    {
        $course = Course::findOrFail($id);

        $data = $request->validated();

        // 🔥 Slug không trùng (bỏ qua chính nó)
        $slug = Str::slug($data['name']);
        $originalSlug = $slug;
        $count = 1;

        while (
            Course::withTrashed()
                ->where('slug', $slug)
                ->where('id', '!=', $course->id)
                ->exists()
        ) {
            $slug = $originalSlug . '-' . $count;
            $count++;
        }

        $data['slug'] = $slug;

        // upload ảnh
        if ($request->hasFile('image')) {
            $data['image'] = $request->file('image')->store('courses', 'public');
        }

        $course->update($data);

        return redirect()->route('courses.index')->with('success', 'Cập nhật thành công');
    }

    // =========================
    // 🗑️ Soft delete
    // =========================
    public function destroy($id)
    {
        Course::destroy($id);
        return back()->with('success', 'Đã xóa');
    }

    // =========================
    // 🗂️ Thùng rác
    // =========================
    public function trash()
    {
        $courses = Course::onlyTrashed()->get();
        return view('courses.trash', compact('courses'));
    }

    // =========================
    // ♻️ Khôi phục
    // =========================
    public function restore($id)
    {
        Course::withTrashed()->findOrFail($id)->restore();
        return back()->with('success', 'Đã khôi phục');
    }

    // =========================
    // ❌ Xóa vĩnh viễn
    // =========================
    public function forceDelete($id)
    {
        Course::withTrashed()->findOrFail($id)->forceDelete();
        return back()->with('success', 'Đã xóa vĩnh viễn');
    }
    public function stats()
{
    $courses = Course::withCount('students')
        ->with('enrollments')
        ->get();

    return view('courses.stats', compact('courses'));
}
}