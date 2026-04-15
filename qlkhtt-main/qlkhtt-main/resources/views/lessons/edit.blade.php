@extends('layouts.master')

@section('content')

<h3>✏️ Sửa bài học</h3>

<form action="{{ route('lessons.update', $lesson->id) }}" method="POST">
    @csrf @method('PUT')

    <div class="mb-3">
        <label>Tiêu đề</label>
        <input type="text" name="title" value="{{ $lesson->title }}" class="form-control">
    </div>

    <div class="mb-3">
        <label>Nội dung</label>
        <textarea name="content" class="form-control">{{ $lesson->content }}</textarea>
    </div>

    <div class="mb-3">
        <label>Video URL</label>
        <input type="text" name="video_url" value="{{ $lesson->video_url }}" class="form-control">
    </div>

    <div class="mb-3">
        <label>Thứ tự</label>
        <input type="number" name="order" value="{{ $lesson->order }}" class="form-control">
    </div>

    <button class="btn btn-primary">Cập nhật</button>

</form>

@endsection