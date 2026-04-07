const translations = {
    en: {
        greeting: "Hello",
        farewell: "Goodbye",
        thankYou: "Thank you",
    },
    zh: {
        greeting: "你好",
        farewell: "再见",
        thankYou: "谢谢",
    },
    es: {
        greeting: "Hola",
        farewell: "Adiós",
        thankYou: "Gracias",
    },
    fr: {
        greeting: "Bonjour",
        farewell: "Au revoir",
        thankYou: "Merci",
    },
    ar: {
        greeting: "مرحبا",
        farewell: "وداعا",
        thankYou: "شكرا",
    }
};

function translate(key, lang) {
    return translations[lang][key] || translations["en"][key];
}

// Example usage
console.log(translate("greeting", "es")); // Output: "Hola"
console.log(translate("thankYou", "zh")); // Output: "谢谢"

export { translate };