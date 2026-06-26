const fs = require('fs');
const readline = require('readline');

const transcriptPath = "C:\\Users\\Jesano Pramathana\\.gemini\\antigravity-ide\\brain\\e0f03029-3d01-47ef-8456-b64840f9596d\\.system_generated\\logs\\transcript_full.jsonl";

async function extractLastData() {
  const fileStream = fs.createReadStream(transcriptPath);
  const rl = readline.createInterface({ input: fileStream, crlfDelay: Infinity });

  let lastEvalData = null;

  for await (const line of rl) {
    if (line.includes('const evaluationData = [')) {
      const parsed = JSON.parse(line);
      const content = parsed.content || '';
      
      const startIndex = content.indexOf('const evaluationData = [');
      if (startIndex !== -1) {
          // Find the matching end brace for the array
          let braceCount = 0;
          let endIndex = -1;
          let started = false;
          for (let i = startIndex; i < content.length; i++) {
              if (content[i] === '[') { braceCount++; started = true; }
              else if (content[i] === ']') { braceCount--; }
              
              if (started && braceCount === 0) {
                  endIndex = i;
                  break;
              }
          }
          
          if (endIndex !== -1) {
              lastEvalData = content.substring(startIndex, endIndex + 1);
          } else {
              // Just grab 10000 chars if we can't find it
              lastEvalData = content.substring(startIndex, startIndex + 10000);
          }
      }
    }
  }
  
  if (lastEvalData) {
      fs.writeFileSync('evalDataLast.txt', lastEvalData);
      console.log('Saved to evalDataLast.txt');
  } else {
      console.log('Not found');
  }
}
extractLastData();
