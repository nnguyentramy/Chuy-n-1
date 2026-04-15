<div class="card shadow-sm mb-3">
    @if(isset($title))
        <div class="card-header bg-dark text-white">
            {{ $title }}
        </div>
    @endif

    <div class="card-body p-0">
        <table class="table table-bordered table-hover align-middle mb-0">
            {{ $slot }}
        </table>
    </div>
</div>