@extends('layouts.master')

@section('content')

<h3>➕ Thêm bài học</h3>

<form action="{{ route('lessons.store') }}" method="POST">
    @csrf

    <input type="hidden" name="course_id" value="{{ $course->id }}">

    <div class="mb-3">
        <label>Tiêu đề</label>
        <input type="text" name="title" class="form-control">
    </div>

    <div class="mb-3">
        <label>Nội dung</label>
        <textarea name="content" class="form-control"></textarea>
    </div>

    <div class="mb-3">
        <label>Video URL</label>
        <input type="text" name="video_url" class="form-control">
    </div>

    <div class="mb-3">
        <label>Thứ tự</label>
        <input type="number" name="order" class="form-control">
    </div>

    <button class="btn btn-success">Lưu</button>
</form>

@endsection