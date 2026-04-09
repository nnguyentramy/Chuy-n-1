@extends('layouts.master')

@section('content')

<h3>📊 Thống kê khóa học</h3>

<div class="card shadow-sm">
    <div class="card-body">

        <table class="table table-bordered text-center">
            <thead class="table-dark">
                <tr>
                    <th>Tên khóa học</th>
                    <th>Số học viên</th>
                    <th>Doanh thu</th>
                </tr>
            </thead>

            <tbody>
                @foreach($courses as $course)
                <tr>
                    <td>{{ $course->name }}</td>

                    <td>
                        {{ $course->students_count }}
                    </td>

                    <td class="text-danger fw-bold">
                        {{ number_format($course->students_count * $course->price) }} đ
                    </td>
                </tr>
                @endforeach
            </tbody>

        </table>

    </div>
</div>

@endsection