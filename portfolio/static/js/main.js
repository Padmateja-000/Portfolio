// Main Custom JavaScript

document.addEventListener('DOMContentLoaded', () => {
    // 1. Initialize AOS Animation Library
    AOS.init({
        duration: 800,
        easing: 'ease-out-cubic',
        once: true,
        offset: 50,
    });

    // 2. Navbar Scroll Effect
    const navbar = document.getElementById('navbar');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('bg-darker/90', 'backdrop-blur-md', 'shadow-lg');
            navbar.classList.remove('bg-transparent', 'py-4');
            navbar.classList.add('py-2');
        } else {
            navbar.classList.remove('bg-darker/90', 'backdrop-blur-md', 'shadow-lg');
            navbar.classList.add('bg-transparent', 'py-4');
            navbar.classList.remove('py-2');
        }
        
        // Active Link Highlighting based on scroll position
        let current = '';
        const sections = document.querySelectorAll('section');
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (scrollY >= (sectionTop - 200)) {
                current = section.getAttribute('id');
            }
        });
        
        document.querySelectorAll('.nav-link').forEach(link => {
            link.classList.remove('active', 'text-accent');
            if (link.getAttribute('href').includes(current)) {
                link.classList.add('active', 'text-accent');
            }
        });
    });

    // 3. Mobile Menu Toggle
    const mobileBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const mobileLinks = document.querySelectorAll('.mobile-nav-link');
    
    if (mobileBtn && mobileMenu) {
        mobileBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
            const icon = mobileBtn.querySelector('i');
            if (mobileMenu.classList.contains('hidden')) {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            } else {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            }
        });
        
        // Close menu on link click
        mobileLinks.forEach(link => {
            link.addEventListener('click', () => {
                mobileMenu.classList.add('hidden');
                const icon = mobileBtn.querySelector('i');
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            });
        });
    }

    // 4. 3D Tilt Effect on Project Cards
    const cards = document.querySelectorAll('.project-card-wrapper');
    
    cards.forEach(cardWrapper => {
        const card = cardWrapper.querySelector('.project-card');
        
        cardWrapper.addEventListener('mousemove', (e) => {
            const rect = cardWrapper.getBoundingClientRect();
            const x = e.clientX - rect.left; // x position within the element.
            const y = e.clientY - rect.top;  // y position within the element.
            
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            
            const rotateX = ((y - centerY) / centerY) * -10; // Max rotation 10deg
            const rotateY = ((x - centerX) / centerX) * 10;
            
            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
        });
        
        cardWrapper.addEventListener('mouseleave', () => {
            card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) scale3d(1, 1, 1)';
        });
    });

    // 5. Hide Django Messages after 5 seconds
    const toasts = document.querySelectorAll('.message-toast');
    if (toasts.length > 0) {
        setTimeout(() => {
            toasts.forEach((toast, index) => {
                setTimeout(() => {
                    toast.classList.remove('translate-x-full', 'opacity-0');
                }, index * 200); // Stagger entry
            });
        }, 100);

        setTimeout(() => {
            toasts.forEach((toast, index) => {
                setTimeout(() => {
                    toast.classList.add('translate-x-full', 'opacity-0');
                    setTimeout(() => { toast.style.display = 'none'; }, 500);
                }, index * 200); // Stagger exit
            });
        }, 5000);
    }
});
