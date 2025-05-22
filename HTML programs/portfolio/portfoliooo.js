// Smooth Scroll for navigation links
document.querySelectorAll('.details1 a').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Form Validation (optional, you can add more validations)
document.getElementById('contactForm').addEventListener('submit', function (e) {
    e.preventDefault();
    
    const username = document.getElementById('user').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('msg').value;

    if (username && email && message) {
        alert('Form Submitted Successfully!');
    } else {
        alert('Please fill in all fields');
    }
});

// Scroll to Top Button
document.getElementById('scrollToTop').addEventListener('click', function (e) {
    e.preventDefault();
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});

// Fade-in effect for elements as user scrolls
window.addEventListener('scroll', () => {
    const fadeInElements = document.querySelectorAll('.fade-in');
    fadeInElements.forEach(element => {
        const elementPosition = element.getBoundingClientRect().top;
        const windowHeight = window.innerHeight;
        
        if (elementPosition < windowHeight - 50) {
            element.classList.add('visible');
        }
    });
});

// Adding the fade-in class to elements when scrolling
document.querySelector('.aboutMe').classList.add('fade-in');
document.querySelector('.contactDTLS').classList.add('fade-in');
