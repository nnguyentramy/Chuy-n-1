@extends('layouts.master')

@section('content')

<h3>➕ Thêm khóa học</h3>

<div class="card shadow-sm">
    <div class="card-body">

        <form action="{{ route('courses.store') }}" method="POST" enctype="multipart/form-data">
            @csrf

            <!-- Tên khóa học -->
            <x-form-input 
                name="name" 
                label="Tên khóa học" 
            />

            <!-- Giá -->
            <x-form-input 
                name="price" 
                label="Giá" 
                type="number"
            />

            <!-- Mô tả -->
            <x-form-textarea 
                name="description" 
                label="Mô tả" 
            />

            <!-- Ảnh -->
            <x-form-file 
                name="image" 
                label="Ảnh khóa học" 
            />

            <!-- Trạng thái -->
            <x-form-select 
                name="status" 
                label="Trạng thái"
                :options="[
                    'draft' => 'Draft',
                    'published' => 'Published'
                ]"
            />

            <div class="mt-3">
                <button class="btn btn-success">💾 Lưu</button>
                <a href="{{ route('courses.index') }}" class="btn btn-secondary">← Quay lại</a>
            </div>

        </form>

    </div>
</div>

@endsection