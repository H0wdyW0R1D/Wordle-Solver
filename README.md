# Wordle-Solver    
Solver for NTY's Wordle game using information theory    

![image](https://github.com/user-attachments/assets/53c90a16-e424-4edb-b774-283927673cc6)

Wordlist: <https://gist.github.com/dracos/dd0668f281e685bad51479e5acaadb93>    
Past Solutions List (goes up to March, 23, 2023): <https://eagerterrier.github.io/previous-wordle-words/chronological.txt>  
    
Using this solver the following was concluded:    
    
## Amount of information gained from words    
This was taken from a subset of over 600 previous Wordle solutions and some common openers.    
Take these words, as well as any words found online, with a grain of salt as reevaluating the same words with a different wordset will yeild different values.  
  
roate: 5.96 bits  
tarse: 5.91 bits  
crate: 5.84 bits  
slate: 5.82 bits  
slate: 5.82 bits  
trace: 5.81 bits  
arise: 5.79 bits  
salet: 5.74 bits  
alter: 5.72 bits  
grate: 5.69 bits  
stale: 5.68 bits  
react: 5.66 bits  
store: 5.65 bits  
cater: 5.61 bits  
saute: 5.6 bits  
crane: 5.59 bits  
trice: 5.59 bits  
scare: 5.56 bits  
atone: 5.56 bits  
great: 5.56 bits  
taper: 5.54 bits  
alone: 5.54 bits  
adore: 5.52 bits  
dealt: 5.52 bits  
trope: 5.51 bits  
stair: 5.5 bits  
solar: 5.47 bits  
train: 5.47 bits  
alien: 5.45 bits  
horse: 5.42 bits  
leapt: 5.42 bits  
pleat: 5.41 bits  
shire: 5.41 bits  
their: 5.39 bits  
coast: 5.38 bits  
saint: 5.38 bits  
triad: 5.37 bits  
lapse: 5.36 bits  
loser: 5.34 bits  
stage: 5.33 bits  
spire: 5.33 bits  
merit: 5.33 bits  
tapir: 5.32 bits  
those: 5.32 bits  
inert: 5.31 bits  
grade: 5.3 bits  
niter: 5.3 bits  
trash: 5.3 bits  
snarl: 5.29 bits  
snarl: 5.29 bits  
spite: 5.29 bits  
islet: 5.29 bits  
poise: 5.28 bits  
acute: 5.28 bits  
smart: 5.28 bits  
heist: 5.27 bits  
wrote: 5.27 bits  
layer: 5.26 bits  
louse: 5.26 bits  
tilde: 5.26 bits  
argue: 5.25 bits  
feast: 5.25 bits  
aside: 5.25 bits  
avert: 5.25 bits  
pause: 5.24 bits  
yearn: 5.23 bits  
smear: 5.23 bits  
tiger: 5.23 bits  
metal: 5.22 bits  
inter: 5.22 bits  
cheat: 5.22 bits  
regal: 5.22 bits  
gloat: 5.21 bits  
panel: 5.21 bits  
trove: 5.2 bits  
crept: 5.2 bits  
plant: 5.2 bits  
delta: 5.19 bits  
pride: 5.19 bits  
clean: 5.18 bits  
trend: 5.18 bits  
farce: 5.18 bits  
alike: 5.18 bits  
smite: 5.18 bits  
death: 5.17 bits  
onset: 5.16 bits  
stead: 5.16 bits  
phase: 5.16 bits  
crave: 5.15 bits  
crave: 5.15 bits  
molar: 5.14 bits  
valet: 5.14 bits  
valet: 5.14 bits  
spiel: 5.14 bits  
dance: 5.13 bits  
spade: 5.13 bits  
treat: 5.13 bits  
ultra: 5.11 bits  
worse: 5.11 bits  
comet: 5.1 bits  
waste: 5.1 bits  
stein: 5.1 bits  
royal: 5.1 bits  
shine: 5.09 bits  
other: 5.09 bits  
print: 5.09 bits  
shame: 5.09 bits  
drain: 5.09 bits  
sedan: 5.09 bits  
opera: 5.09 bits  
unite: 5.09 bits  
goner: 5.08 bits  
thorn: 5.08 bits  
hoard: 5.08 bits  
prime: 5.08 bits  
rouge: 5.08 bits  
cider: 5.08 bits  
house: 5.07 bits  
tease: 5.07 bits  
frame: 5.06 bits  
giant: 5.06 bits  
brine: 5.06 bits  
recap: 5.06 bits  
maple: 5.06 bits  
gripe: 5.05 bits  
sweat: 5.05 bits  
rogue: 5.05 bits  
staid: 5.05 bits  
dream: 5.04 bits  
trite: 5.04 bits  
sloth: 5.04 bits  
crust: 5.03 bits  
email: 5.03 bits  
rainy: 5.02 bits  
rainy: 5.02 bits  
heron: 5.02 bits  
trawl: 5.02 bits  
gamer: 5.02 bits  
moist: 5.02 bits  
matey: 5.01 bits  
story: 5.01 bits  
smelt: 5.01 bits  
flair: 5.0 bits  
credo: 5.0 bits  
float: 5.0 bits  
repay: 5.0 bits  
lunar: 5.0 bits  
hairy: 4.99 bits  
radio: 4.99 bits  
probe: 4.99 bits  
grime: 4.99 bits  
glean: 4.99 bits  
point: 4.99 bits  
pilot: 4.98 bits  
grave: 4.98 bits  
sower: 4.98 bits  
trait: 4.98 bits  
chant: 4.97 bits  
creak: 4.97 bits  
ulcer: 4.97 bits  
blame: 4.97 bits  
shard: 4.97 bits  
aloft: 4.97 bits  
gruel: 4.96 bits  
brake: 4.96 bits  
flirt: 4.95 bits  
front: 4.95 bits  
manor: 4.95 bits  
ample: 4.95 bits  
retch: 4.94 bits  
cigar: 4.94 bits  
snout: 4.94 bits  
homer: 4.94 bits  
audit: 4.93 bits  
shake: 4.93 bits  
mealy: 4.92 bits  
apron: 4.92 bits  
chest: 4.92 bits  
today: 4.92 bits  
stand: 4.92 bits  
craze: 4.91 bits  
depot: 4.91 bits  
medal: 4.91 bits  
chute: 4.91 bits  
count: 4.9 bits  
usage: 4.9 bits  
cargo: 4.9 bits  
weary: 4.9 bits  
labor: 4.9 bits  
sugar: 4.89 bits  
adieu: 4.89 bits  
third: 4.89 bits  
scorn: 4.89 bits  
solve: 4.89 bits  
brave: 4.89 bits  
cloth: 4.88 bits  
peach: 4.88 bits  
prove: 4.87 bits  
naive: 4.87 bits  
upset: 4.87 bits  
model: 4.87 bits  
croak: 4.87 bits  
stove: 4.87 bits  
marsh: 4.86 bits  
braid: 4.86 bits  
berth: 4.86 bits  
tepid: 4.86 bits  
first: 4.86 bits  
aloud: 4.85 bits  
adopt: 4.85 bits  
claim: 4.85 bits  
groin: 4.85 bits  
skirt: 4.85 bits  
inept: 4.84 bits  
antic: 4.84 bits  
irony: 4.84 bits  
spray: 4.84 bits  
piety: 4.83 bits  
moult: 4.83 bits  
tiara: 4.83 bits  
adobe: 4.83 bits  
forge: 4.83 bits  
rebut: 4.83 bits  
twice: 4.82 bits  
twine: 4.82 bits  
chard: 4.82 bits  
fault: 4.81 bits  
start: 4.81 bits  
scour: 4.81 bits  
drive: 4.8 bits  
amber: 4.8 bits  
altar: 4.8 bits  
purge: 4.8 bits  
threw: 4.79 bits  
poker: 4.79 bits  
finer: 4.79 bits  
rhino: 4.79 bits  
scrap: 4.79 bits  
voice: 4.78 bits  
corny: 4.78 bits  
sneak: 4.77 bits  
blurt: 4.77 bits  
scald: 4.77 bits  
viral: 4.77 bits  
grove: 4.77 bits  
aorta: 4.76 bits  
girth: 4.76 bits  
asset: 4.76 bits  
power: 4.76 bits  
unlit: 4.76 bits  
liver: 4.75 bits  
mince: 4.75 bits  
nasty: 4.75 bits  
olive: 4.75 bits  
froth: 4.75 bits  
foyer: 4.75 bits  
there: 4.74 bits  
parer: 4.74 bits  
chafe: 4.74 bits  
perch: 4.73 bits  
baton: 4.73 bits  
break: 4.73 bits  
glory: 4.73 bits  
golem: 4.73 bits  
biome: 4.73 bits  
aptly: 4.72 bits  
baker: 4.72 bits  
vault: 4.72 bits  
unmet: 4.71 bits  
charm: 4.71 bits  
mount: 4.71 bits  
greet: 4.71 bits  
rival: 4.71 bits  
crank: 4.71 bits  
heady: 4.71 bits  
sonic: 4.71 bits  
agate: 4.71 bits  
vital: 4.7 bits  
usher: 4.7 bits  
foray: 4.7 bits  
round: 4.7 bits  
agree: 4.7 bits  
spoke: 4.69 bits  
forth: 4.69 bits  
chord: 4.69 bits  
cramp: 4.69 bits  
troll: 4.69 bits  
retro: 4.68 bits  
mourn: 4.68 bits  
fresh: 4.68 bits  
admit: 4.68 bits  
lemon: 4.68 bits  
hinge: 4.67 bits  
pinto: 4.67 bits  
piney: 4.67 bits  
yield: 4.67 bits  
tangy: 4.66 bits  
money: 4.66 bits  
spike: 4.66 bits  
swirl: 4.66 bits  
primo: 4.65 bits  
badge: 4.65 bits  
infer: 4.65 bits  
surly: 4.64 bits  
angry: 4.64 bits  
birth: 4.64 bits  
abate: 4.62 bits  
paper: 4.62 bits  
prize: 4.62 bits  
erode: 4.62 bits  
extra: 4.61 bits  
robin: 4.61 bits  
scold: 4.61 bits  
panic: 4.61 bits  
could: 4.61 bits  
rhyme: 4.61 bits  
flout: 4.6 bits  
quart: 4.6 bits  
bloke: 4.59 bits  
atoll: 4.59 bits  
midst: 4.59 bits  
focal: 4.59 bits  
depth: 4.59 bits  
thyme: 4.59 bits  
sound: 4.59 bits  
inane: 4.58 bits  
inane: 4.58 bits  
heath: 4.58 bits  
impel: 4.58 bits  
bland: 4.58 bits  
rusty: 4.58 bits  
glove: 4.58 bits  
hyper: 4.57 bits  
choke: 4.57 bits  
movie: 4.56 bits  
maize: 4.56 bits  
month: 4.55 bits  
spend: 4.55 bits  
tipsy: 4.54 bits  
audio: 4.54 bits  
above: 4.54 bits  
yacht: 4.54 bits  
whine: 4.54 bits  
epoch: 4.54 bits  
wince: 4.53 bits  
beady: 4.53 bits  
manly: 4.53 bits  
shirk: 4.53 bits  
surer: 4.52 bits  
field: 4.52 bits  
torso: 4.52 bits  
tough: 4.52 bits  
tacit: 4.52 bits  
exist: 4.52 bits  
group: 4.52 bits  
lapel: 4.51 bits  
youth: 4.51 bits  
flesh: 4.51 bits  
quiet: 4.51 bits  
vague: 4.51 bits  
chief: 4.51 bits  
light: 4.5 bits  
apple: 4.5 bits  
midge: 4.49 bits  
shawl: 4.49 bits  
masse: 4.49 bits  
world: 4.49 bits  
rebus: 4.48 bits  
gorge: 4.48 bits  
sting: 4.47 bits  
abase: 4.47 bits  
crimp: 4.47 bits  
denim: 4.47 bits  
duvet: 4.47 bits  
basic: 4.47 bits  
caulk: 4.47 bits  
egret: 4.46 bits  
taunt: 4.46 bits  
riper: 4.44 bits  
elope: 4.44 bits  
crass: 4.44 bits  
fetus: 4.44 bits  
natal: 4.43 bits  
stomp: 4.43 bits  
lusty: 4.43 bits  
humor: 4.42 bits  
valid: 4.41 bits  
cling: 4.41 bits  
growl: 4.41 bits  
flume: 4.41 bits  
lofty: 4.4 bits  
doubt: 4.4 bits  
moose: 4.4 bits  
siege: 4.4 bits  
goose: 4.4 bits  
totem: 4.39 bits  
input: 4.39 bits  
polka: 4.39 bits  
perky: 4.38 bits  
pound: 4.38 bits  
drink: 4.37 bits  
elder: 4.37 bits  
stink: 4.37 bits  
steed: 4.37 bits  
fleet: 4.37 bits  
grimy: 4.36 bits  
rupee: 4.36 bits  
cache: 4.36 bits  
leery: 4.36 bits  
aphid: 4.36 bits  
belch: 4.35 bits  
briar: 4.35 bits  
guild: 4.35 bits  
spicy: 4.35 bits  
being: 4.35 bits  
shrug: 4.35 bits  
gauze: 4.35 bits  
squat: 4.34 bits  
favor: 4.34 bits  
ivory: 4.34 bits  
slung: 4.34 bits  
twang: 4.34 bits  
label: 4.34 bits  
linen: 4.34 bits  
stool: 4.34 bits  
bribe: 4.33 bits  
watch: 4.33 bits  
feign: 4.33 bits  
prick: 4.33 bits  
salad: 4.33 bits  
shall: 4.33 bits  
jaunt: 4.33 bits  
aroma: 4.32 bits  
carry: 4.32 bits  
droll: 4.32 bits  
begin: 4.32 bits  
leave: 4.32 bits  
magic: 4.31 bits  
syrup: 4.31 bits  
night: 4.31 bits  
badly: 4.31 bits  
vigor: 4.3 bits  
agape: 4.3 bits  
stick: 4.3 bits  
brisk: 4.3 bits  
exult: 4.29 bits  
clown: 4.29 bits  
class: 4.29 bits  
godly: 4.29 bits  
bring: 4.29 bits  
ahead: 4.28 bits  
crazy: 4.28 bits  
belie: 4.28 bits  
pithy: 4.28 bits  
ought: 4.27 bits  
bench: 4.26 bits  
study: 4.26 bits  
human: 4.25 bits  
equal: 4.25 bits  
serve: 4.25 bits  
slump: 4.25 bits  
gaudy: 4.25 bits  
agora: 4.25 bits  
cross: 4.25 bits  
wooer: 4.25 bits  
joust: 4.25 bits  
askew: 4.24 bits  
tryst: 4.24 bits  
sweet: 4.24 bits  
oxide: 4.24 bits  
unfit: 4.23 bits  
tasty: 4.23 bits  
stout: 4.23 bits  
motor: 4.23 bits  
arbor: 4.23 bits  
major: 4.22 bits  
dowry: 4.22 bits  
truss: 4.22 bits  
champ: 4.22 bits  
theme: 4.21 bits  
parry: 4.21 bits  
shrub: 4.21 bits  
spell: 4.21 bits  
album: 4.21 bits  
sleek: 4.2 bits  
black: 4.2 bits  
brink: 4.2 bits  
blush: 4.2 bits  
dozen: 4.19 bits  
bayou: 4.19 bits  
helix: 4.19 bits  
elude: 4.18 bits  
woken: 4.18 bits  
shown: 4.18 bits  
sever: 4.17 bits  
ruder: 4.17 bits  
whelp: 4.17 bits  
dutch: 4.17 bits  
fixer: 4.16 bits  
havoc: 4.16 bits  
shock: 4.16 bits  
frock: 4.15 bits  
robot: 4.15 bits  
musty: 4.15 bits  
lying: 4.14 bits  
lilac: 4.14 bits  
toxic: 4.14 bits  
dwarf: 4.13 bits  
woven: 4.13 bits  
valve: 4.13 bits  
gecko: 4.13 bits  
glass: 4.12 bits  
slosh: 4.12 bits  
libel: 4.12 bits  
unfed: 4.12 bits  
gouge: 4.12 bits  
donor: 4.11 bits  
marry: 4.11 bits  
itchy: 4.11 bits  
revel: 4.11 bits  
opium: 4.1 bits  
found: 4.1 bits  
pique: 4.1 bits  
boost: 4.09 bits  
patty: 4.09 bits  
where: 4.08 bits  
catch: 4.08 bits  
using: 4.07 bits  
showy: 4.06 bits  
dodge: 4.06 bits  
gulch: 4.05 bits  
flail: 4.05 bits  
zesty: 4.05 bits  
spill: 4.05 bits  
koala: 4.04 bits  
essay: 4.04 bits  
fling: 4.04 bits  
focus: 4.04 bits  
usual: 4.04 bits  
renew: 4.03 bits  
hatch: 4.03 bits  
colon: 4.03 bits  
proxy: 4.03 bits  
query: 4.03 bits  
banal: 4.01 bits  
bleed: 4.01 bits  
enema: 4.01 bits  
avail: 4.01 bits  
floor: 4.0 bits  
tibia: 4.0 bits  
quasi: 3.99 bits  
blown: 3.98 bits  
wrung: 3.98 bits  
seedy: 3.98 bits  
bough: 3.98 bits  
evade: 3.98 bits  
butch: 3.98 bits  
axiom: 3.97 bits  
waltz: 3.97 bits  
vouch: 3.97 bits  
chill: 3.96 bits  
larva: 3.96 bits  
pluck: 3.96 bits  
flock: 3.95 bits  
photo: 3.94 bits  
conic: 3.94 bits  
debug: 3.94 bits  
canny: 3.93 bits  
tweed: 3.92 bits  
squad: 3.91 bits  
awful: 3.91 bits  
awake: 3.9 bits  
ferry: 3.9 bits  
flick: 3.9 bits  
batty: 3.89 bits  
glyph: 3.89 bits  
alpha: 3.88 bits  
thumb: 3.88 bits  
roomy: 3.87 bits  
undue: 3.87 bits  
abbey: 3.87 bits  
digit: 3.86 bits  
unify: 3.86 bits  
ionic: 3.85 bits  
ninth: 3.85 bits  
pinky: 3.85 bits  
fishy: 3.85 bits  
skimp: 3.85 bits  
allow: 3.84 bits  
coyly: 3.84 bits  
error: 3.83 bits  
vodka: 3.81 bits  
staff: 3.81 bits  
apply: 3.81 bits  
epoxy: 3.81 bits  
chunk: 3.8 bits  
delve: 3.79 bits  
comma: 3.79 bits  
aging: 3.79 bits  
loopy: 3.77 bits  
skill: 3.77 bits  
worry: 3.77 bits  
sweep: 3.77 bits  
naval: 3.76 bits  
enjoy: 3.76 bits  
needy: 3.76 bits  
howdy: 3.76 bits  
swill: 3.75 bits  
picky: 3.75 bits  
dandy: 3.75 bits  
whack: 3.75 bits  
condo: 3.75 bits  
karma: 3.74 bits  
pooch: 3.73 bits  
floss: 3.73 bits  
cheek: 3.72 bits  
duchy: 3.72 bits  
belly: 3.72 bits  
kiosk: 3.71 bits  
knoll: 3.71 bits  
judge: 3.7 bits  
fjord: 3.69 bits  
outdo: 3.68 bits  
fewer: 3.68 bits  
blurb: 3.67 bits  
quirk: 3.67 bits  
wacky: 3.67 bits  
gloom: 3.67 bits  
usurp: 3.66 bits  
soggy: 3.66 bits  
fungi: 3.64 bits  
clock: 3.64 bits  
offal: 3.64 bits  
hunky: 3.63 bits  
cinch: 3.63 bits  
flood: 3.61 bits  
salsa: 3.61 bits  
pixie: 3.61 bits  
gawky: 3.6 bits  
forgo: 3.6 bits  
happy: 3.58 bits  
click: 3.58 bits  
hutch: 3.58 bits  
kebab: 3.57 bits  
folly: 3.55 bits  
nymph: 3.55 bits  
wedge: 3.53 bits  
eject: 3.53 bits  
khaki: 3.51 bits  
cacao: 3.49 bits  
abyss: 3.48 bits  
ruddy: 3.48 bits  
cynic: 3.47 bits  
lowly: 3.46 bits  
fifty: 3.45 bits  
booze: 3.45 bits  
excel: 3.43 bits  
mucky: 3.42 bits  
gully: 3.4 bits  
pulpy: 3.4 bits  
aback: 3.37 bits  
knock: 3.35 bits  
hippy: 3.35 bits  
cluck: 3.34 bits  
beefy: 3.29 bits  
whoop: 3.26 bits  
motto: 3.25 bits  
maxim: 3.21 bits  
foggy: 3.15 bits  
humph: 3.07 bits  
madam: 3.04 bits  
daddy: 3.0 bits  
sissy: 2.99 bits  
bluff: 2.97 bits  
gamma: 2.88 bits  
buggy: 2.87 bits  
boozy: 2.8 bits  
mimic: 2.75 bits  
booby: 2.72 bits  
civic: 2.6 bits  
vivid: 2.51 bits  
fluff: 2.47 bits  
mummy: 2.37 bits  
  
## Frequency of letters:    
This is useful when trying to determine a good starting word, but other information gained from some words (such as letter positioning) is more useful.    
    
e: 7455    
s: 7319    
a: 7128    
o: 5212    
r: 4714    
i: 4381    
l: 3780    
t: 3707    
n: 3478    
u: 2927    
d: 2735    
p: 2436    
m: 2414    
y: 2400    
c: 2246    
h: 1993    
g: 1864    
b: 1849    
k: 1753    
f: 1240    
w: 1127    
v: 801    
z: 503    
j: 342    
x: 326    
q: 145  
