@extends('layouts.master')

@section('content')

<h3 class="mb-4">📊 Dashboard</h3>

<div class="row">

    <!-- Tổng khóa học -->
    <div class="col-md-3">
        <div class="card text-white bg-primary mb-3">
            <div class="card-body text-center">
                <h5>Tổng khóa học</h5>
                <h3>{{ $totalCourses }}</h3>
            </div>
        </div>
    </div>

    <!-- Tổng học viên -->
    <div class="col-md-3">
        <div class="card text-white bg-success mb-3">
            <div class="card-body text-center">
                <h5>Học viên</h5>
                <h3>{{ $totalStudents }}</h3>
            </div>
        </div>
    </div>

    <!-- Doanh thu -->
    <div class="col-md-3">
        <div class="card text-white bg-warning mb-3">
            <div class="card-body text-center">
                <h5>Doanh thu</h5>
                <h3>{{ number_format($totalRevenue) }} đ</h3>
            </div>
        </div>
    </div>

    <!-- Top khóa học -->
    <div class="col-md-3">
        <div class="card text-white bg-danger mb-3">
            <div class="card-body text-center">
                <h5>Top khóa học</h5>
                <small>
                    {{ $topCourse->name ?? 'Chưa có' }}
                </small>
                <br>
                <strong>{{ $topCourse->students_count ?? 0 }} HV</strong>
            </div>
        </div>
    </div>

</div>

<!-- 5 khóa học mới -->
<div class="card shadow-sm">
    <div class="card-header">
        🎓 5 khóa học mới
    </div>

    <div class="card-body">

        <table class="table table-bordered">
            <thead class="table-dark">
                <tr>
                    <th>Tên</th>
                    <th>Giá</th>
                    <th>Trạng thái</th>
                </tr>
            </thead>

            <tbody>
                @foreach($latestCourses as $course)
                <tr>
                    <td>{{ $course->name }}</td>
                    <td>{{ number_format($course->price) }} đ</td>
                    <td>
                        <x-badge-status :status="$course->status" />
                    </td>
                </tr>
                @endforeach
            </tbody>

        </table>

    </div>
</div>

@endsection