// Back to Top button
const backToTop = document.createElement("div");
backToTop.id = "backToTop";
backToTop.innerText = "↑";
document.body.appendChild(backToTop);

window.addEventListener("scroll", () => {
    if (window.scrollY > 200) {
        backToTop.style.display = "block";
    } else {
        backToTop.style.display = "none";
    }
});

backToTop.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
});

// Animate sections on scroll
const sections = document.querySelectorAll("section");

const revealOnScroll = () => {
    const triggerBottom = window.innerHeight * 0.85;

    sections.forEach(sec => {
        const boxTop = sec.getBoundingClientRect().top;

        if (boxTop < triggerBottom) {
            sec.classList.add("visible");
        } else {
            sec.classList.remove("visible");
        }
    });
};

sections.forEach(sec => sec.classList.add("fade-in"));
window.addEventListener("scroll", revealOnScroll);
window.addEventListener("load", revealOnScroll);

// Table row click interaction
document.querySelectorAll("table tr").forEach(row => {
    row.addEventListener("click", () => {
        const product = row.cells[0]?.innerText;
        if (product) {
            alert(`You clicked on: ${product}`);
        }
    });
});

