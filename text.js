const words = ["          ","C R E A T E", "R E A D", "U P D A T E", "D E L E T E", "C R E A T E", "R E A D", "U P D A T E", "D E L E T E"];
const textElement = document.getElementById("text");
let wordIndex = 0;
let charIndex = 0;

function type() {
    if (charIndex < words[wordIndex].length) {
        textElement.textContent += words[wordIndex].charAt(charIndex);
        charIndex++;
        setTimeout(type, 100); // Adjust typing speed here (milliseconds)
    } else {
        setTimeout(erase, 1000); // Delay before erasing
    }
}

function erase() {
    if (charIndex > 0) {
        textElement.textContent = words[wordIndex].substring(0, charIndex - 1);
        charIndex--;
        setTimeout(erase, 50); // Adjust erasing speed here (milliseconds)
    } else {
        wordIndex = (wordIndex + 1) % words.length;
        setTimeout(type, 500); // Delay before typing the next word
    }
}

type(); // Start the animation
