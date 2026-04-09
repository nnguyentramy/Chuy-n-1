<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Quản lý khóa học</title>

    <!-- Bootstrap 5 -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">

<nav class="navbar navbar-dark bg-dark">
    <div class="container d-flex justify-content-between">

        <!-- Logo -->
        <a class="navbar-brand" href="{{ route('courses.index') }}">
            🎓 Course Management
        </a>

        <!-- 🔥 Menu -->
        <div>
            <a href="{{ route('dashboard') }}" class="btn btn-outline-light me-2">
                📊 Dashboard
            </a>

            <a href="{{ route('courses.index') }}" class="btn btn-outline-light me-2">
                📚 Courses
            </a>

            <a href="{{ route('enrollments.create') }}" class="btn btn-outline-light">
                👨‍🎓 Enroll
            </a>
        </div>

    </div>
</nav>

<div class="container mt-4">

    <!-- Alert -->
    <x-alert />

    @yield('content')

</div>

<!-- Bootstrap JS -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>