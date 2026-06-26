const fs = require('fs');
const readline = require('readline');

const transcriptPath = "C:\\Users\\Jesano Pramathana\\.gemini\\antigravity-ide\\brain\\e0f03029-3d01-47ef-8456-b64840f9596d\\.system_generated\\logs\\transcript_full.jsonl";

async function extractOriginalData() {
  const fileStream = fs.createReadStream(transcriptPath);
  const rl = readline.createInterface({ input: fileStream, crlfDelay: Infinity });

  for await (const line of rl) {
    if (line.includes('const evaluationData = [')) {
      const parsed = JSON.parse(line);
      const content = parsed.content || '';
      
      const startIndex = content.indexOf('const evaluationData = [');
      if (startIndex !== -1) {
          const substring = content.substring(startIndex, startIndex + 5000);
          fs.writeFileSync('evalDataOriginal.txt', substring);
          console.log('Saved to evalDataOriginal.txt');
          return;
      }
    }
  }
}
extractOriginalData();
