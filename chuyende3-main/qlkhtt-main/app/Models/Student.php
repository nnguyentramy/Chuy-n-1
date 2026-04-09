<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use App\Models\Course;
use App\Models\Enrollment;  

class Student extends Model
{
    protected $fillable = ['name', 'email'];

    // 1 student có nhiều enrollment
    public function enrollments()
    {
        return $this->hasMany(Enrollment::class);
    }

    // nhiều course qua enrollment
    public function courses()
    {
        return $this->belongsToMany(Course::class, 'enrollments');
    }
}