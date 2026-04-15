<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\SoftDeletes;
use App\Models\Lesson;
use App\Models\Enrollment;
use App\Models\Student;

class Course extends Model
{
    use SoftDeletes;

    protected $fillable = [
        'name',
        'slug',
        'price',
        'description',
        'image',
        'status'
    ];

    // =========================
    // 🔗 RELATIONSHIP
    // =========================

    // 1 course có nhiều lesson
    public function lessons()
    {
        return $this->hasMany(Lesson::class);
    }

    // 1 course có nhiều enrollment
    public function enrollments()
    {
        return $this->hasMany(Enrollment::class);
    }

    // nhiều student qua bảng trung gian enrollments
    public function students()
    {
        return $this->belongsToMany(Student::class, 'enrollments');
    }

    // =========================
    // 🚀 SCOPE (PHẦN 3.5)
    // =========================

    // chỉ lấy khóa đã publish
    public function scopePublished($query)
    {
        return $query->where('status', 'published');
    }

    // lọc theo khoảng giá
    public function scopePriceBetween($query, $min, $max)
    {
        return $query->whereBetween('price', [$min, $max]);
    }
}