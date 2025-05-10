function toggleDarkMode() {
    document.documentElement.classList.toggle('dark-theme');
    
    // Alterna o ícone do botão
    const themeIcon = document.getElementById('theme-icon');
    if (document.documentElement.classList.contains('dark-theme')) {
        themeIcon.classList.remove('fa-moon');
        themeIcon.classList.add('fa-sun');
    } else {
        themeIcon.classList.remove('fa-sun');
        themeIcon.classList.add('fa-moon');
    }
}