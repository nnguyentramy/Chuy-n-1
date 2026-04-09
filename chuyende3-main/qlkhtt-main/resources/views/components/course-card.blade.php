@props(['course'])

<div class="card shadow-sm h-100">
    
    {{-- Ảnh --}}
    @if($course->image)
        <img src="{{ asset('storage/'.$course->image) }}" 
             class="card-img-top" 
             style="height:200px; object-fit:cover;">
    @endif

    <div class="card-body">
        <h5 class="card-title">{{ $course->name }}</h5>

        <p class="text-danger fw-bold">
            {{ number_format($course->price) }} đ
        </p>

        {{-- Badge --}}
        <x-badge-status :status="$course->status" />

        <p class="mt-2 text-muted">
            {{ $course->lessons_count ?? 0 }} bài học
        </p>
    </div>

    <div class="card-footer text-center">

        <a href="{{ route('lessons.index', $course->id) }}" 
           class="btn btn-sm btn-secondary">
            📚 Bài học
        </a>

        <a href="{{ route('enrollments.index', $course->id) }}" 
           class="btn btn-sm btn-success">
            👨‍🎓 Học viên
        </a>

    </div>

</div>