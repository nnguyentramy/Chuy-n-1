<?php

namespace App\Http\Requests;

use Illuminate\Contracts\Validation\ValidationRule;
use Illuminate\Foundation\Http\FormRequest;

class StoreCourseRequest extends FormRequest
{
    public function authorize()
    {
        return true;
    }

    public function rules()
    {
        return [
            'name' => 'required|min:3',
            'price' => 'required|numeric|min:1',
            'description' => 'nullable',
            'image' => 'nullable|image',
            'status' => 'required|in:draft,published'
        ];
    }
}
