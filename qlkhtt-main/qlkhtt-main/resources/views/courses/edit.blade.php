@extends('layouts.master')

@section('content')

<h3>✏️ Sửa khóa học</h3>

<div class="card shadow-sm">
    <div class="card-body">

        <form action="{{ route('courses.update', $course->id) }}" method="POST" enctype="multipart/form-data">
            @csrf @method('PUT')

            <div class="mb-3">
                <label>Tên khóa học</label>
                <input type="text" name="name" class="form-control" value="{{ $course->name }}">
            </div>

            <div class="mb-3">
                <label>Giá</label>
                <input type="number" name="price" class="form-control" value="{{ $course->price }}">
            </div>

            <div class="mb-3">
                <label>Mô tả</label>
                <textarea name="description" class="form-control">{{ $course->description }}</textarea>
            </div>

            <div class="mb-3">
                <label>Ảnh hiện tại</label><br>
                @if($course->image)
                    <img src="{{ asset('storage/'.$course->image) }}" width="100">
                @endif
            </div>

            <div class="mb-3">
                <label>Ảnh mới</label>
                <input type="file" name="image" class="form-control">
            </div>

            <div class="mb-3">
                <label>Trạng thái</label>
                <select name="status" class="form-select">
                    <option value="draft" {{ $course->status == 'draft' ? 'selected' : '' }}>Draft</option>
                    <option value="published" {{ $course->status == 'published' ? 'selected' : '' }}>Published</option>
                </select>
            </div>

            <button class="btn btn-primary">Cập nhật</button>
            <a href="{{ route('courses.index') }}" class="btn btn-secondary">Quay lại</a>

        </form>

    </div>
</div>

@endsection