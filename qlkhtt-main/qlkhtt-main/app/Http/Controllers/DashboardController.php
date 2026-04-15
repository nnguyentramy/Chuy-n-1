<?php

namespace App\Http\Controllers;

use App\Models\Course;
use App\Models\Student;
use App\Models\Enrollment;

class DashboardController extends Controller
{
    public function index()
    {
        // Tổng khóa học
        $totalCourses = Course::count();

        // Tổng học viên
        $totalStudents = Student::count();

        // Tổng doanh thu (giả định: mỗi enrollment = 1 lần mua)
        $totalRevenue = Enrollment::join('courses', 'enrollments.course_id', '=', 'courses.id')
            ->sum('courses.price');

        // Khóa học nhiều học viên nhất
        $topCourse = Course::withCount('students')
            ->orderByDesc('students_count')
            ->first();

        // 5 khóa học mới
        $latestCourses = Course::latest()->take(5)->get();

        return view('dashboard', compact(
            'totalCourses',
            'totalStudents',
            'totalRevenue',
            'topCourse',
            'latestCourses'
        ));
    }
}