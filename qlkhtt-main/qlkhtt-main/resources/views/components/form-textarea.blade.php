<div class="mb-3">
    <label class="form-label">{{ $label }}</label>

    <textarea 
        name="{{ $name }}"
        class="form-control @error($name) is-invalid @enderror"
    >{{ old($name, $value ?? '') }}</textarea>

    @error($name)
        <div class="invalid-feedback">
            {{ $message }}
        </div>
    @enderror
</div>