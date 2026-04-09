<div class="bg-dark text-white p-3" style="width:250px; min-height:100vh">
    <h4 class="mb-4">🎓 CMS</h4>

    <ul class="nav flex-column">

        <li class="nav-item mb-2">
            <a href="{{ route('courses.index') }}" class="nav-link text-white">
                📚 Courses
            </a>
        </li>

        <li class="nav-item mb-2">
            <a href="{{ route('lessons.index', 1) }}" class="nav-link text-white">
                🎥 Lessons
            </a>
        </li>

        <li class="nav-item mb-2">
            <a href="{{ route('enrollments.create') }}" class="nav-link text-white">
                👨‍🎓 Enrollments
            </a>
        </li>

    </ul>
</div>