@extends('layouts.master')

@section('content')

<h3>📝 Đăng ký khóa học</h3>

<form action="{{ route('enrollments.store') }}" method="POST">
    @csrf

    <div class="mb-3">
        <label>Chọn khóa học</label>
        <select name="course_id" class="form-select">
            @foreach($courses as $course)
                <option value="{{ $course->id }}">{{ $course->name }}</option>
            @endforeach
        </select>
    </div>

    <div class="mb-3">
        <label>Tên học viên</label>
        <input type="text" name="name" class="form-control">
    </div>

    <div class="mb-3">
        <label>Email</label>
        <input type="email" name="email" class="form-control">
    </div>

    <button class="btn btn-success">Đăng ký</button>

</form>

@endsection