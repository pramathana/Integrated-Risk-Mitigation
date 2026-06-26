const fs = require('fs');
const readline = require('readline');

const transcriptPath = "C:\\Users\\Jesano Pramathana\\.gemini\\antigravity-ide\\brain\\e0f03029-3d01-47ef-8456-b64840f9596d\\.system_generated\\logs\\transcript_full.jsonl";

async function extractUserInput() {
  const fileStream = fs.createReadStream(transcriptPath);
  const rl = readline.createInterface({ input: fileStream, crlfDelay: Infinity });

  for await (const line of rl) {
    if (line.includes('"type":"USER_INPUT"')) {
        const parsed = JSON.parse(line);
        if (parsed.content.includes("evaluationData")) {
            fs.writeFileSync('userInputEval.txt', parsed.content);
            console.log('Saved to userInputEval.txt');
            return;
        }
    }
  }
}
extractUserInput();
