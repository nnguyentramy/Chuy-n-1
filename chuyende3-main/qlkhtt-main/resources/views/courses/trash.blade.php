@extends('layouts.master')

@section('content')

<h3>🗑️ Thùng rác khóa học</h3>

@if($courses->isEmpty())
    <div class="alert alert-warning">
        Không có dữ liệu trong thùng rác
    </div>
@else

<div class="card shadow-sm">
    <div class="card-body">

        <table class="table table-bordered">
            <thead class="table-dark text-center">
                <tr>
                    <th>Tên</th>
                    <th>Giá</th>
                    <th>Trạng thái</th>
                    <th width="200">Hành động</th>
                </tr>
            </thead>

            <tbody>
                @foreach($courses as $course)
                <tr>
                    <td>{{ $course->name }}</td>
                    <td>{{ number_format($course->price) }} đ</td>
                    <td>{{ $course->status }}</td>

                    <td class="text-center">
                        <!-- Khôi phục -->
                        <a href="{{ route('courses.restore', $course->id) }}"
                           class="btn btn-success btn-sm">
                            Khôi phục
                        </a>

                        <!-- Xóa vĩnh viễn -->
                        <form action="{{ route('courses.forceDelete', $course->id) }}"
                              method="POST" class="d-inline">
                            @csrf @method('DELETE')
                            <button class="btn btn-danger btn-sm"
                                onclick="return confirm('Xóa vĩnh viễn?')">
                                Xóa vĩnh viễn
                            </button>
                        </form>
                    </td>
                </tr>
                @endforeach
            </tbody>

        </table>

    </div>
</div>

@endif

<a href="{{ route('courses.index') }}" class="btn btn-secondary mt-3">
    ← Quay lại
</a>

@endsection