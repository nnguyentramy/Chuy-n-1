@extends('layouts.master')

@section('content')

<h3>📚 Bài học của: {{ $course->name }}</h3>

<a href="{{ route('lessons.create', $course->id) }}" class="btn btn-primary mb-3">
    + Thêm bài học
</a>

<table class="table table-bordered">
    <thead class="table-dark">
        <tr>
            <th>STT</th>
            <th>Tiêu đề</th>
            <th>Video</th>
            <th>Hành động</th>
        </tr>
    </thead>

    <tbody>
        @foreach($lessons as $lesson)
        <tr>
            <td>{{ $lesson->order }}</td>
            <td>{{ $lesson->title }}</td>
            <td>
                @if($lesson->video_url)
                    <a href="{{ $lesson->video_url }}" target="_blank">Xem</a>
                @endif
            </td>
            <td>
                <a href="{{ route('lessons.edit', $lesson->id) }}" class="btn btn-warning btn-sm">Sửa</a>

                <form action="{{ route('lessons.destroy', $lesson->id) }}" method="POST" class="d-inline">
                    @csrf @method('DELETE')
                    <button class="btn btn-danger btn-sm">Xóa</button>
                </form>
            </td>
        </tr>
        @endforeach
    </tbody>
</table>

@endsection