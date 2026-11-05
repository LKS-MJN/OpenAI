import test from 'node:test';
import assert from 'node:assert/strict';
import {questions,getEnding,endings} from '../story.js';
test('Every complete route reaches a valid ending; all three endings are reachable',()=>{
 const reached=new Set();let routes=0;
 function walk(step,scores){if(step===questions.length){const ending=getEnding(scores);assert.ok(endings[ending]);reached.add(ending);routes++;return}for(const choice of questions[step].choices){assert.equal(choice.length,3);assert.ok(choice[0]&&choice[2]);walk(step+1,{...scores,[choice[1]]:scores[choice[1]]+1})}}
 walk(0,{trust:0,ambition:0,suspicion:0});assert.equal(routes,729);assert.equal(reached.size,3);
});
for(const [answer,expected] of [[0,'hired'],[1,'heir'],[2,'escape']])test(`Consistent answer ${answer+1} reaches ${expected}`,()=>{const scores={trust:0,ambition:0,suspicion:0};for(const q of questions)scores[q.choices[answer][1]]++;assert.equal(getEnding(scores),expected)});
