**FEATURES TODO**
--
- Create tweets on a canvas - like drawing on paper.
- Could implement a basic MS paint and upload media directly drawn in the app

- Start in museum lobby -> sign into guest book -> pop-up window for twitter authorization
- Enter museum, displays text posts as framed paintings
- Facing a text post and clicking 'enter' will display the author and their bio, as an artist would in a museum
- Exits to return to the lobby exist every 10 or so tweets
- Add surprise rooms for fun (you can collect these themed rooms - they have easter egg content, maybe our favorite tweets?)
- Highlight canvases when a tweet has been edited(?)
- Have museum theme packs
- Sponsors display as pixel art on canvases (or theme packs!)

**TODO**
- Reformat backend to py for twscrape? 


########
1. Run `python3.11 -m venv .venv` 
   1. `python3.11` is the desired python version
   2. `-m` says run python script called venv
   3. Give the argument `.venv`
   4. Makes virtual environment (a collection of packages) at `.venv` directory
2. Activate .venv directory `source .venv/bin/activate`
   1. `source` says run everything at this file and inject it into current command prompt
   2. Use whatever directory the ve is made in
3. (One time) Create a `requirements.txt` file
   1. List all libraries inside
   2. Run `pip install -r requirements.txt`