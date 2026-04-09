<div class="mb-3">
    <label class="form-label">{{ $label }}</label>

    <select name="{{ $name }}" class="form-select">
        @foreach($options as $key => $value)
            <option value="{{ $key }}" 
                {{ old($name, $selected ?? '') == $key ? 'selected' : '' }}>
                {{ $value }}
            </option>
        @endforeach
    </select>
</div>