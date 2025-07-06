// 1) Import packages
const express = require('express');
const axios = require('axios');
require('dotenv').config(); // Load .env variables

// 2) Create Express app
const app = express();
app.use(express.json()); // Parse JSON request bodies
app.use(express.static('public')); // Serve static files (your HTML, CSS, JS)

// 3) Get your Gemini API key
const API_KEY = process.env.GEMINI_API_KEY;

// 4) POST endpoint: frontend will call this to talk to Gemini
app.post('/api/chat', async (req, res) => {
  const userMessage = req.body.message; // Get message from frontend

  try {
    const response = await axios.post(
      `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=${API_KEY}`,
      {
        contents: [
          {
            role: "user",
            parts: [{ text: userMessage }]
          }
        ]
      },
      { headers: { "Content-Type": "application/json" } }
    );

    const reply = response.data.candidates[0].content.parts[0].text;
    res.json({ reply }); // Send back to frontend

  } catch (error) {
    console.error(error.response ? error.response.data : error.message);
    res.status(500).json({ error: "Failed to get response from Gemini API." });
  }
});

// 5) Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`✅ Server running at http://localhost:${PORT}`);
});
