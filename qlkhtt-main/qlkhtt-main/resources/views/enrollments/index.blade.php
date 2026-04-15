@extends('layouts.master')

@section('content')

<h3>👨‍🎓 Học viên khóa: {{ $course->name }}</h3>

<p><strong>Tổng số học viên: {{ $students->count() }}</strong></p>

<table class="table table-bordered">
    <thead class="table-dark">
        <tr>
            <th>Tên</th>
            <th>Email</th>
        </tr>
    </thead>

    <tbody>
        @forelse($students as $student)
        <tr>
            <td>{{ $student->name }}</td>
            <td>{{ $student->email }}</td>
        </tr>
        @empty
        <tr>
            <td colspan="2" class="text-center">Chưa có học viên</td>
        </tr>
        @endforelse
    </tbody>
</table>

@endsection