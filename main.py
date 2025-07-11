from fastapi import FastAPI

app = FastAPI()

@app.get("/profile")
def get_profile():
    return {
    "name": "👩‍💻 Muskan Fatima",
    "title": "🚀 Next.js & Tailwind CSS Enthusiast | 🎨 Frontend Developer in Training",
    "email": "📧 mushiifatima3456@gmail.com",
    "location": "📍 Pakistan",
    "education": {
        "degree": "🎓 Bachelor of Science",
        "certification": "📜 GenEng - The Cloud Applied Generative AI Engineering",
        "graduation_year": "🎓 2026"
    },
    "skills": [
    "⚛️ Next.js", "📜 TypeScript", "🎨 Tailwind CSS", "⚛️ React.js",
    "📜 JavaScript", "🐍 Python", "🔧 Git & GitHub", "🎨 Figma",
    "🔗 API Integration", "🧩 Problem-Solving", "⚡ FastAPI",
    "🧠 Core Web Vitals", "🤖 Gemini API", "🧠 LangChain (learning)",
    "⚙️ Agent Framework", "🧪 Unit Testing"
],
    "projects": [
        
    {
        "name": "🧾 MF Resume Builder",
        "description": "⚙️ Builds professional resumes with modern UI and multiple template logic.",
        "technologies": ["⚛️ Next.js", "📜 TypeScript", "🎨 Tailwind CSS"],
        "live": "https://mf-resume.vercel.app"
    },
    {
        "name": "🚗 Mornet Car Rent Website",
        "description": "🌐 A sleek car rental platform with smooth UI and interactive experience.",
        "technologies": ["⚛️ Next.js", "🎨 Tailwind CSS"],
        "live": "https://mornet.vercel.app"
    },
    {
        "name": "🕌 Ramadan Coding Night",
        "description": "💻 20-day coding challenge project series built with Python and FastAPI.",
        "technologies": ["🐍 Python", "⚡ FastAPI", "🔗 Chainlit", "📊 Streamlit", "🤖 Gemini"],
        "github": "https://github.com/muskan-fatim/Ramdan_coding_night"
    },
    {
        "name": "✍️ Blog Website with Comments",
        "description": "🗞️ A dynamic blog site built as a class project, includes comment section.",
        "technologies": ["⚛️ Next.js", "🎨 Tailwind CSS", "📝 Markdown"],
        "live": "https://blog-web-git-main-muskan-fatim.vercel.app"
    },
    {
        "name": "🌐 Python Translator",
        "description": "🔤 Translates text between languages using a simple Python script and external APIs.",
        "technologies": ["🐍 Python", "🔗 Deep Translator API"],
        "github": "https://github.com/muskan-fatim/Python-Translator"
    },
   
    {
        "name": "🎫 Conference Ticket Generator",
        "description": "📩 Generates personalized PDF tickets using user input and FastAPI.",
        "technologies": ["🐍 Python", "⚡ FastAPI", "🧩 ReportLab"],
        "github": "https://github.com/muskan-fatim/conference-ticket-generator"
    

        },
        {
            "name": "🍔 FoodPanda Clone",
            "description": "🌐 A fully responsive clone of the FoodPanda website.",
            "technologies": ["⚛️ React.js", "🎨 CSS"],
            "github": "🔗 https://github.com/muskan-fatim/FoodPanda-Clone"
        },
        {
            "name": "💡 Simple API",
            "description": "📜 FastAPI project that returns random motivational quotes.",
            "technologies": ["🐍 Python", "⚡ FastAPI"],
            "github": "🔗 https://github.com/muskan-fatim/Simple-API"
        }
    ],
"experience": [
    {
        "role": "👩‍💻 Contributor",
        "organization": "🌍 GirlScript Summer of Code",
        "duration": "📆 Oct 2024 - Nov 2024",
        "description": "🤝 Contributed to open-source projects and collaborated with developers globally."
    },
    {
        "role": "👩‍💻 Hackathon Participant",
        "organization": "⚡ Hackathon 3",
        "duration": "📆 2025",
        "description": "🚀 Built innovative apps with team collaboration under time pressure."
    },
    {
        "role": "💡 Volunteer Contributor",
        "organization": "📘 GIAIC - GenAI Certification Program",
        "duration": "📆 2025",
        "description": "🎯 Assisted fellow students, shared resources, and contributed to community learning activities."
    },
    {
        "role": "🎓 Campus Ambassador",
        "organization": "🌍 GirlScript Summer of Code 2025",
        "duration": "📆 2025",
        "description": "📣 Promoted the program, helped onboard contributors, and represented GSSoC at campus level."
    }
],
        
       "certifications": [
    {
        "name": "🏅 Deployed Typed Function Using TypeScript",
        "issuer": "🎓 Microsoft",
        "date": "📆 May 28, 2024"
    },
    {
        "name": "🏅 Contributor Certificate - GSSoC 2024",
        "issuer": "🌍 GirlScript Summer of Code",
        "date": "📆 November 2024"
    }

    ],
    "languages": {
        "English": "🗣️ Advanced",
        "Urdu": "🗣️ Fluent"
    },
    "social_links": {
        "github": "🐙 https://github.com/muskan-fatim",
        "linkedin": "🔗 https://www.linkedin.com/in/muskan-fatima-ab90732b7/",
        "portfolio": "🌐 https://protofilo-2.vercel.app/"
    },
    "github_repositories": [
        {
            "name": "🌙 Ramdan Coding Night",
            "description": "💻 A challenge aimed at improving coding skills during the holy month.",
            "technologies": ["🐍 Python", "🤖 Prompt", "🔗 Gemini", "⚡ UV", "⚡ FastAPI", "📊 Streamlit", "🔗 Chain"],
            "github_url": "🔗 https://github.com/muskan-fatim/Ramdan_coding_night"
        },
        {
            "name": "🍔 FoodPanda Clone",
            "description": "🌐 A fully responsive clone of the FoodPanda website.",
            "technologies": ["⚛️ Next.js", "🎨 CSS"],
            "github_url": "🔗 https://github.com/muskan-fatim/FoodPanda-Clone"
        },
        {
            "name": "📄 Resume Generator",
            "description": "📝 A tool that generates resumes from templates with complex logic and customization.",
            "technologies": ["⚛️ Next.js", "📜 TypeScript", "🎨 CSS"],
            "github_url": "🔗 https://github.com/muskan-fatim/Resume-Generator"
        },
        {
            "name": "🌍 Protofilo_2",
            "description": "💼 My personal portfolio created with Next.js and TypeScript.",
            "technologies": ["⚛️ Next.js", "📜 TypeScript", "🎨 CSS"],
            "github_url": "🔗 https://github.com/muskan-fatim/Protofilo_2"
        },
        {
            "name": "⏳ CLI Countdown App",
            "description": "🕒 A command-line interface countdown application.",
            "technologies": ["📜 TypeScript", "🎛️ Inquirer"],
            "github_url": "🔗 https://github.com/muskan-fatim/CLI-Countdown-App"
        },
        {
            "name": "📚 Student Management CLI",
            "description": "🎓 A CLI-based student management system.",
            "technologies": ["📜 TypeScript", "🎛️ Inquirer"],
            "github_url": "🔗 https://github.com/muskan-fatim/Student-Management-CLI"
        }
    ]
}
