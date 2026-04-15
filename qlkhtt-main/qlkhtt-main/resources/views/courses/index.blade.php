@extends('layouts.master')

@section('content')

<div class="d-flex justify-content-between mb-3">
    <h3>📚 Danh sách khóa học</h3>
    <div>
        <a href="{{ route('courses.create') }}" class="btn btn-primary">+ Thêm</a>
        <a href="{{ route('courses.trash') }}" class="btn btn-warning">Thùng rác</a>
    </div>
</div>

<!-- 🔍 FORM TÌM KIẾM + LỌC -->
<form method="GET" class="row mb-3">

    <!-- Tên -->
    <div class="col-md-3">
        <input type="text" name="name" 
            value="{{ request('name') }}"
            class="form-control" 
            placeholder="Tên khóa học">
    </div>

    <!-- Giá -->
    <div class="col-md-2">
        <input type="number" name="price" 
            value="{{ request('price') }}"
            class="form-control" 
            placeholder="Giá tối đa">
    </div>

    <!-- Trạng thái -->
    <div class="col-md-2">
        <select name="status" class="form-select">
            <option value="">-- Trạng thái --</option>
            <option value="draft" {{ request('status')=='draft'?'selected':'' }}>Draft</option>
            <option value="published" {{ request('status')=='published'?'selected':'' }}>Published</option>
        </select>
    </div>

    <!-- Sắp xếp -->
    <div class="col-md-3">
        <select name="sort" class="form-select">
            <option value="">-- Sắp xếp --</option>
            <option value="price_asc" {{ request('sort')=='price_asc'?'selected':'' }}>Giá tăng</option>
            <option value="price_desc" {{ request('sort')=='price_desc'?'selected':'' }}>Giá giảm</option>
            <option value="students" {{ request('sort')=='students'?'selected':'' }}>Nhiều học viên</option>
            <option value="newest" {{ request('sort')=='newest'?'selected':'' }}>Mới nhất</option>
        </select>
    </div>

    <!-- Button -->
    <div class="col-md-2">
        <button class="btn btn-primary w-100">🔍 Tìm</button>
    </div>

</form>

<x-table title="Danh sách khóa học">

    <thead class="table-dark text-center">
        <tr>
            <th>Ảnh</th>
            <th>Tên</th>
            <th>Giá</th>
            <th>Trạng thái</th>
            <th>Bài học</th>
            <th width="260">Hành động</th>
        </tr>
    </thead>

    <tbody>
        @forelse($courses as $course)
        <tr>
            <td class="text-center">
                @if($course->image)
                    <img src="{{ asset('storage/'.$course->image) }}" 
                         width="80" 
                         class="rounded">
                @endif
            </td>

            <td>{{ $course->name }}</td>

            <td class="text-danger fw-bold">
                {{ number_format($course->price) }} đ
            </td>

            <td class="text-center">
                <x-badge-status :status="$course->status" />
            </td>

            <td class="text-center">
                {{ $course->lessons_count }}
            </td>

            <td class="text-center">

                <a href="{{ route('lessons.index', $course->id) }}" 
                   class="btn btn-sm btn-secondary">
                    📚 Bài học
                </a>

                <a href="{{ route('enrollments.index', $course->id) }}" 
                   class="btn btn-sm btn-success">
                   👨‍🎓 Học viên
                </a>

                <a href="{{ route('courses.edit', $course->id) }}" 
                   class="btn btn-sm btn-info">
                    ✏️ Sửa
                </a>

                <form action="{{ route('courses.destroy', $course->id) }}" 
                      method="POST" class="d-inline">
                    @csrf @method('DELETE')
                    <button class="btn btn-sm btn-danger"
                        onclick="return confirm('Xóa khóa học?')">
                        🗑️ Xóa
                    </button>
                </form>

            </td>
        </tr>
        @empty
        <tr>
            <td colspan="6" class="text-center text-muted">
                Chưa có khóa học nào
            </td>
        </tr>
        @endforelse
    </tbody>

</x-table>

<div class="mt-3">
    {{ $courses->links() }}
</div>

@endsection