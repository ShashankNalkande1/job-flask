// Dashboard JavaScript functionality

// Toast notification system
function showToast(message, type = 'info') {
    const toastHtml = `
        <div class="toast align-items-center text-white bg-${type === 'error' ? 'danger' : type === 'success' ? 'success' : 'primary'} border-0" role="alert" aria-live="assertive" aria-atomic="true">
            <div class="d-flex">
                <div class="toast-body">
                    ${message}
                </div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
        </div>
    `;
    
    // Create toast container if it doesn't exist
    let toastContainer = document.getElementById('toast-container');
    if (!toastContainer) {
        toastContainer = document.createElement('div');
        toastContainer.id = 'toast-container';
        toastContainer.className = 'toast-container position-fixed bottom-0 end-0 p-3';
        toastContainer.style.zIndex = '1050';
        document.body.appendChild(toastContainer);
    }
    
    // Add toast to container
    toastContainer.insertAdjacentHTML('beforeend', toastHtml);
    
    // Show toast
    const toastElement = toastContainer.lastElementChild;
    const toast = new bootstrap.Toast(toastElement);
    toast.show();
    
    // Remove toast element after it's hidden
    toastElement.addEventListener('hidden.bs.toast', () => {
        toastElement.remove();
    });
}

// Loading state management
function setButtonLoading(button, loading = true) {
    if (loading) {
        button.dataset.originalText = button.innerHTML;
        button.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Loading...';
        button.disabled = true;
    } else {
        button.innerHTML = button.dataset.originalText;
        button.disabled = false;
    }
}

// Enhanced API call function with error handling
async function apiCall(url, options = {}) {
    try {
        const response = await fetch(url, {
            headers: {
                'Content-Type': 'application/json',
                ...options.headers
            },
            ...options
        });
        
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.error || 'Something went wrong');
        }
        
        return data;
    } catch (error) {
        throw error;
    }
}

// Form validation helpers
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function validateRequired(value) {
    return value && value.trim().length > 0;
}

// Initialize tooltips and popovers
document.addEventListener('DOMContentLoaded', function() {
    // Initialize Bootstrap tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Initialize Bootstrap popovers
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });
    
    // Add smooth scrolling to all internal links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
});

// Theme management
function toggleTheme() {
    const body = document.body;
    const isDark = body.classList.contains('bg-dark');
    
    if (isDark) {
        body.classList.remove('bg-dark', 'text-light');
        localStorage.setItem('theme', 'light');
        showToast('Switched to light theme', 'success');
    } else {
        body.classList.add('bg-dark', 'text-light');
        localStorage.setItem('theme', 'dark');
        showToast('Switched to dark theme', 'success');
    }
}

// Load saved theme on page load
document.addEventListener('DOMContentLoaded', function() {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('bg-dark', 'text-light');
    }
});

// Dashboard card interactions
document.addEventListener('DOMContentLoaded', function() {
    // Add hover effects to dashboard cards
    const cards = document.querySelectorAll('.dashboard-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
});

// Auto-save form data
function autoSaveForm(formId, interval = 30000) {
    const form = document.getElementById(formId);
    if (!form) return;
    
    setInterval(() => {
        const formData = new FormData(form);
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value;
        });
        
        localStorage.setItem(`autosave_${formId}`, JSON.stringify(data));
        showToast('Form data auto-saved', 'info');
    }, interval);
}

// Restore auto-saved form data
function restoreFormData(formId) {
    const savedData = localStorage.getItem(`autosave_${formId}`);
    if (!savedData) return;
    
    try {
        const data = JSON.parse(savedData);
        const form = document.getElementById(formId);
        
        Object.keys(data).forEach(key => {
            const field = form.querySelector(`[name="${key}"]`);
            if (field) {
                field.value = data[key];
            }
        });
        
        showToast('Form data restored', 'success');
    } catch (error) {
        console.error('Error restoring form data:', error);
    }
}

// Onboarding form validation and enhancement
const OnboardingValidator = {
    // Step 1 validation rules
    step1: {
        first_name: {
            required: true,
            minLength: 2,
            pattern: /^[a-zA-Z\s]+$/,
            message: 'First name must be at least 2 characters and contain only letters'
        },
        last_name: {
            required: true,
            minLength: 2,
            pattern: /^[a-zA-Z\s]+$/,
            message: 'Last name must be at least 2 characters and contain only letters'
        },
        email: {
            required: true,
            pattern: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
            message: 'Please enter a valid email address'
        },
        phone: {
            required: true,
            pattern: /^[\+]?[1-9][\d]{0,15}$/,
            message: 'Please enter a valid phone number'
        }
    },
    
    // Step 2 validation rules
    step2: {
        company_name: {
            required: true,
            minLength: 2,
            message: 'Company name must be at least 2 characters long'
        },
        industry: {
            required: true,
            message: 'Please select an industry'
        },
        size: {
            required: true,
            message: 'Please select company size'
        }
    },
    
    // Step 3 validation rules
    step3: {
        theme: {
            required: true,
            message: 'Please select a theme preference'
        },
        layout: {
            required: true,
            message: 'Please select a layout preference'
        }
    },
    
    // Validate a single field
    validateField(fieldName, value, step) {
        const rules = this[`step${step}`][fieldName];
        if (!rules) return { valid: true };
        
        // Check required
        if (rules.required && (!value || value.trim().length === 0)) {
            return { valid: false, message: `${fieldName.replace('_', ' ')} is required` };
        }
        
        // Check minimum length
        if (rules.minLength && value && value.length < rules.minLength) {
            return { valid: false, message: rules.message || `Minimum ${rules.minLength} characters required` };
        }
        
        // Check pattern
        if (rules.pattern && value && !rules.pattern.test(value)) {
            return { valid: false, message: rules.message || 'Invalid format' };
        }
        
        return { valid: true };
    },
    
    // Validate entire form
    validateForm(formElement, step) {
        const formData = new FormData(formElement);
        const errors = {};
        let hasErrors = false;
        
        // Get validation rules for current step
        const stepRules = this[`step${step}`];
        if (!stepRules) return { valid: true, errors: {} };
        
        // Validate each field
        Object.keys(stepRules).forEach(fieldName => {
            const value = formData.get(fieldName);
            const validation = this.validateField(fieldName, value, step);
            
            if (!validation.valid) {
                errors[fieldName] = validation.message;
                hasErrors = true;
            }
        });
        
        return { valid: !hasErrors, errors };
    }
};

// Real-time field validation
function setupFieldValidation(formId, step) {
    const form = document.getElementById(formId);
    if (!form) return;
    
    // Add event listeners to all form fields
    const fields = form.querySelectorAll('input, select, textarea');
    fields.forEach(field => {
        // Validate on blur
        field.addEventListener('blur', function() {
            validateSingleField(this, step);
        });
        
        // Clear validation on focus
        field.addEventListener('focus', function() {
            clearFieldValidation(this);
        });
        
        // Real-time validation for text inputs
        if (field.type === 'text' || field.type === 'email' || field.type === 'tel') {
            field.addEventListener('input', debounce(function() {
                validateSingleField(this, step);
            }, 500));
        }
    });
}

// Validate single field and show feedback
function validateSingleField(field, step) {
    const validation = OnboardingValidator.validateField(field.name, field.value, step);
    const fieldContainer = field.closest('.mb-3') || field.closest('.form-group');
    
    if (!validation.valid) {
        field.classList.add('is-invalid');
        field.classList.remove('is-valid');
        
        // Show error message
        let feedback = fieldContainer.querySelector('.invalid-feedback');
        if (!feedback) {
            feedback = document.createElement('div');
            feedback.className = 'invalid-feedback';
            field.parentNode.appendChild(feedback);
        }
        feedback.textContent = validation.message;
    } else if (field.value) {
        field.classList.add('is-valid');
        field.classList.remove('is-invalid');
        
        // Remove error message
        const feedback = fieldContainer.querySelector('.invalid-feedback');
        if (feedback) {
            feedback.remove();
        }
    }
}

// Clear field validation
function clearFieldValidation(field) {
    field.classList.remove('is-invalid', 'is-valid');
    const fieldContainer = field.closest('.mb-3') || field.closest('.form-group');
    const feedback = fieldContainer.querySelector('.invalid-feedback');
    if (feedback) {
        feedback.remove();
    }
}

// Debounce function for performance
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Enhanced form submission with validation
function setupFormSubmission(formId, step) {
    const form = document.getElementById(formId);
    if (!form) return;
    
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Validate form
        const validation = OnboardingValidator.validateForm(form, step);
        
        if (!validation.valid) {
            // Show field errors
            Object.keys(validation.errors).forEach(fieldName => {
                const field = form.querySelector(`[name="${fieldName}"]`);
                if (field) {
                    field.classList.add('is-invalid');
                    const fieldContainer = field.closest('.mb-3') || field.closest('.form-group');
                    
                    let feedback = fieldContainer.querySelector('.invalid-feedback');
                    if (!feedback) {
                        feedback = document.createElement('div');
                        feedback.className = 'invalid-feedback';
                        field.parentNode.appendChild(feedback);
                    }
                    feedback.textContent = validation.errors[fieldName];
                }
            });
            
            showToast('Please correct the errors below', 'error');
            return;
        }
        
        // Show loading state
        const submitButton = form.querySelector('button[type="submit"]');
        setButtonLoading(submitButton, true);
        
        // Submit form
        setTimeout(() => {
            form.submit();
        }, 500); // Small delay to show loading state
    });
}

// Progress animation
function animateProgress(targetPercent, duration = 1000) {
    const progressBar = document.querySelector('.progress-bar');
    if (!progressBar) return;
    
    const startPercent = 0;
    const startTime = Date.now();
    
    function updateProgress() {
        const elapsed = Date.now() - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const currentPercent = startPercent + (targetPercent - startPercent) * progress;
        
        progressBar.style.width = currentPercent + '%';
        progressBar.setAttribute('aria-valuenow', currentPercent);
        progressBar.textContent = Math.round(currentPercent) + '%';
        
        if (progress < 1) {
            requestAnimationFrame(updateProgress);
        }
    }
    
    requestAnimationFrame(updateProgress);
}

// Initialize onboarding enhancements
document.addEventListener('DOMContentLoaded', function() {
    // Detect current page and step
    const path = window.location.pathname;
    let currentStep = null;
      if (path.includes('/onboarding/step1')) {
        currentStep = 1;
        setupFieldValidation('onboarding-form', 1);
        setupFormSubmission('onboarding-form', 1);
        restoreFormData('onboarding-form');
        autoSaveForm('onboarding-form', 15000); // Auto-save every 15 seconds
        animateProgress(33);
        addFieldEnhancements();
    } else if (path.includes('/onboarding/step2')) {
        currentStep = 2;
        setupFieldValidation('onboarding-form', 2);
        setupFormSubmission('onboarding-form', 2);
        restoreFormData('onboarding-form');
        autoSaveForm('onboarding-form', 15000);
        animateProgress(66);
        addFieldEnhancements();
    } else if (path.includes('/onboarding/step3')) {
        currentStep = 3;
        setupFieldValidation('onboarding-form', 3);
        setupFormSubmission('onboarding-form', 3);
        restoreFormData('onboarding-form');
        autoSaveForm('onboarding-form', 15000);
        animateProgress(100);
        addFieldEnhancements();
    }
    
    // Add step completion celebration
    if (currentStep === 3) {
        setTimeout(() => {
            showToast('🎉 Almost there! Just one more step!', 'success');
        }, 1000);
    }
});

// Form field enhancements
function addFieldEnhancements() {
    // Add character counter for text inputs
    document.querySelectorAll('input[type="text"], textarea').forEach(input => {
        if (input.hasAttribute('maxlength')) {
            const maxLength = input.getAttribute('maxlength');
            const counter = document.createElement('small');
            counter.className = 'form-text text-muted character-counter';
            counter.textContent = `0/${maxLength}`;
            
            input.parentNode.appendChild(counter);
            
            input.addEventListener('input', function() {
                counter.textContent = `${this.value.length}/${maxLength}`;
                
                if (this.value.length > maxLength * 0.9) {
                    counter.classList.add('text-warning');
                } else {
                    counter.classList.remove('text-warning');
                }
            });
        }
    });
    
    // Add tooltips to form labels
    document.querySelectorAll('label').forEach(label => {
        const fieldName = label.getAttribute('for');
        const tooltips = {
            'first_name': 'Enter your first name as it appears on official documents',
            'last_name': 'Enter your last name or surname',
            'email': 'We\'ll use this email for important notifications',
            'phone': 'Include country code if outside your country',
            'company_name': 'Official name of your company or organization',
            'industry': 'Select the industry that best describes your business',
            'size': 'Approximate number of employees in your organization',
            'theme': 'Choose between light and dark color schemes',
            'layout': 'Select how you want your dashboard to be organized'
        };
        
        if (tooltips[fieldName]) {
            label.setAttribute('data-bs-toggle', 'tooltip');
            label.setAttribute('data-bs-placement', 'top');
            label.setAttribute('title', tooltips[fieldName]);
        }
    });
}
