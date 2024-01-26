<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Name - Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>

    <header>
        <h1>Your Name</h1>
        <p>Web Developer</p>
    </header>

    <nav>
        <ul>
            <li><a href="#about">About Me</a></li>
            <li><a href="#projects">Projects</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>

    <section id="about">
        <h2>About Me</h2>
        <p>
            Welcome to my portfolio! I am a passionate web developer with a focus on creating meaningful and user-friendly web applications.
        </p>
    </section>

    <section id="projects">
        <h2>Projects</h2>
        <div class="project">
            <h3>Project 1</h3>
            <p>Description of Project 1.</p>
        </div>
        <div class="project">
            <h3>Project 2</h3>
            <p>Description of Project 2.</p>
        </div>
    </section>

    <section id="contact">
        <h2>Contact</h2>
        <p>Feel free to reach out to me. Let's connect!</p>
        <p>Email: your.email@example.com</p>
        <p>LinkedIn: [Your LinkedIn Profile]</p>
    </section>

    <footer>
        <p>&copy; 2022 Your Name</p>
    </footer>

</body>
</html>

/* styles.css */

body {
    font-family: 'Arial', sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: white;
    text-align: center;
    padding: 1em;
}

nav {
    background-color: #555;
    color: white;
    padding: 0.5em;
}

nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
}

nav a {
    text-decoration: none;
    color: white;
    padding: 1em;
    display: block;
}

nav a:hover {
    background-color: #777;
}

section {
    padding: 2em;
}

section h2 {
    color: #333;
}

footer {
    background-color: #555;
    color: white;
    text-align: center;
    padding: 1em;
    position: fixed;
    bottom: 0;
    width: 100%;
}
