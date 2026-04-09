<?php

namespace App\Http\Controllers;

use App\Models\Lesson;
use App\Models\Course;
use Illuminate\Http\Request;

class LessonController extends Controller
{
    // Danh sách theo khóa học
    public function index($course_id)
    {
        $course = Course::findOrFail($course_id);
        $lessons = Lesson::where('course_id', $course_id)
            ->orderBy('order')
            ->get();

        return view('lessons.index', compact('course', 'lessons'));
    }

    // Form thêm
    public function create($course_id)
    {
        $course = Course::findOrFail($course_id);
        return view('lessons.create', compact('course'));
    }

    // Lưu
    public function store(Request $request)
    {
        $request->validate([
            'title' => 'required',
            'order' => 'required|integer'
        ]);

        Lesson::create($request->all());

        return back()->with('success', 'Thêm bài học thành công');
    }

    // Form sửa
    public function edit($id)
    {
        $lesson = Lesson::findOrFail($id);
        return view('lessons.edit', compact('lesson'));
    }

    // Update
    public function update(Request $request, $id)
    {
        $lesson = Lesson::findOrFail($id);

        $lesson->update($request->all());

        return back()->with('success', 'Cập nhật thành công');
    }

    // Xóa
    public function destroy($id)
    {
        Lesson::destroy($id);
        return back()->with('success', 'Đã xóa');
    }
}