<?php

namespace App\Http\Controllers;

use App\Models\Course;
use App\Models\Student;
use App\Models\Enrollment;
use Illuminate\Http\Request;

class EnrollmentController extends Controller
{
    // Form đăng ký
    public function create()
    {
        $courses = Course::all();
        return view('enrollments.create', compact('courses'));
    }

    // Lưu đăng ký
    public function store(Request $request)
    {
        $request->validate([
            'course_id' => 'required',
            'name' => 'required',
            'email' => 'required|email'
        ]);

        // tìm hoặc tạo student
        $student = Student::firstOrCreate(
            ['email' => $request->email],
            ['name' => $request->name]
        );

        // tạo enrollment
        Enrollment::create([
            'course_id' => $request->course_id,
            'student_id' => $student->id
        ]);

        return back()->with('success', 'Đăng ký thành công');
    }

    // Danh sách học viên theo khóa
    public function index($course_id)
    {
        $course = Course::findOrFail($course_id);
        $students = $course->students;

        return view('enrollments.index', compact('course', 'students'));
    }
}