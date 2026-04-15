<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\CourseController;
use App\Http\Controllers\LessonController;
use App\Http\Controllers\EnrollmentController;
use App\Http\Controllers\DashboardController;
Route::get('/', function () {
    return view('welcome');
});


Route::get('courses-trash', [CourseController::class, 'trash'])->name('courses.trash');
Route::get('courses-restore/{id}', [CourseController::class, 'restore'])->name('courses.restore');

Route::resource('courses', CourseController::class);
Route::get('courses-trash', [CourseController::class, 'trash'])->name('courses.trash');
Route::get('courses-restore/{id}', [CourseController::class, 'restore'])->name('courses.restore');

// Xóa vĩnh viễn (bonus)
Route::delete('courses-force-delete/{id}', [CourseController::class, 'forceDelete'])->name('courses.forceDelete');

Route::resource('courses', CourseController::class);

Route::get('lessons/{id}/edit', [LessonController::class, 'edit'])->name('lessons.edit');
Route::put('lessons/{id}', [LessonController::class, 'update'])->name('lessons.update');
Route::delete('lessons/{id}', [LessonController::class, 'destroy'])->name('lessons.destroy');
Route::get('courses/{id}/lessons', [LessonController::class, 'index'])->name('lessons.index');
Route::get('courses/{id}/lessons/create', [LessonController::class, 'create'])->name('lessons.create');
Route::post('lessons/store', [LessonController::class, 'store'])->name('lessons.store');

// đăng ký
Route::get('enrollments/create', [EnrollmentController::class, 'create'])->name('enrollments.create');
Route::post('enrollments/store', [EnrollmentController::class, 'store'])->name('enrollments.store');

// danh sách theo khóa học
Route::get('courses/{id}/students', [EnrollmentController::class, 'index'])->name('enrollments.index');

Route::get('/dashboard', [DashboardController::class, 'index'])->name('dashboard');

Route::get('/stats', [App\Http\Controllers\CourseController::class, 'stats'])->name('courses.stats');