Title: Internship Lessons
Date: 2024-03-23 7:37pm
Category: Misc
Tags: misc
Slug: intern-lessons
Summary: Some lessons from my previous internships


<script src="{attach}/scripts/nutshelldev.js"></script>
<script>
Nutshell.setOptions({
    dontEmbedHeadings: true, // If 'true', removes the "embed this as a nutshell" option on headings
});
</script>

## some lessons from my internships

these are things i found useful through my internships and are probably good guidelines for anyone doing one.

---

I'll be testing [Nutshell](https://github.com/ncase/nutshell) out! When you see a link like [:this](#note1), click on it to expand it.

---

1. **document, document, document**
    - every day, i made a page to dump notes, which included things like:
        - running log of what i accomplished / meetings i went to (+ meeting notes)
        - notes on how to do something
            - eg: how to spin up a new server
        - musings on potential ways to accomplish something 
            - eg: to build this pipeline, i could use x to connect to y server and send data to z
        - section for jotting down what you need to do the next day / future goals
        - anything i needed to copy paste 
            - eg: list of server names
        - these logs are very helpful for your final presentation / project report
    - i also had pages for specific tools/languages so i could note down useful commands
        - eg: i made a page with useful clickhouse queries and docs i found myself referencing a lot
    - [:example for a day](#notesExample)
  
2. **set up expectations / goals and project timelines asap**
    - understand why your project(s) is important
        - why / how is your project providing value? can you measure that? what does success look like?
    - find people that will benefit or have to change their workflow because of your project and talk to them (and follow up on their feedback!)
    - if you're struggling, set up a more granular timeline and ask what your mentor thinks to see if you're on the right track
   
3. **talk to people! set up coffee chats with anyone doing anything you find interesting**
    - given a topic / area you want chat about, your manager / team members will help you find people to talk to if you aren't sure who
    - come with a list of questions you want to talk about; here's [my list](https://docs.google.com/spreadsheets/d/1WzSHwv_hTlsfgAC48OTBDUfOw5NFwRwygPLtYjf2DY4/){: .blue-link} for coffee chats
    - similarly, if you hear about interesting projects during stand up, you can set up a quick meeting with your team member and have them run through it with you 
  
4. **have understandable commits, code, and readme**
    - people are looking at them and judging you based on it because these are the main things you are there to create
    - ask your mentor about how they style commits and comments
        - might be worth looking at [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/){: .blue-link}
            - [:tldr](#conventional)
    - make everything you create as user friendly as possible
        - note down how to run your code, potential failures and how to remedy them
        - you will not be there to explain how anything works in three months

5. **read about the tools you're going to be using**
    - if you're not sure where to find the best resources, ask for reading material and internal docs about tools and libraries
    - listen to talks about similar projects in other companies or how your team functions in other companies
    - do not spend too much time rabbit holing into tools or the codebase at the expense of doing things
    - look up style guides for languages you're using to learn best practices
        - ex: list of google's [style guides](https://google.github.io/styleguide/){: .blue-link}, uber's [go guide](https://github.com/uber-go/guide/blob/master/style.md){: .blue-link}

6. **ask good questions**
    - ask for lots of help if you need it! it's more productive to ask than spend an hour hunting online for an answer 
    - make sure to google your question before you ask
        - if you didn't find anything useful, ask for help and mention what you discovered online
    - anything else i have to say has been said better by julia evans: [(1)](https://jvns.ca/blog/good-questions/){: .blue-link} [(2)](https://jvns.ca/blog/2021/10/21/how-to-get-useful-answers-to-your-questions/){: .blue-link}

7. **if you find something annoying, see if you can quickly automate it**
    - bash is your friend
    - if you can't do it quickly, ask your mentor if it's worthwhile to spend time automating it so other people can use your script

8. **socialize with other interns, go to intern events**
    - at least there's free food

---

note: i have never done a swe internship. make of this what you will.

## :x note1
hi!

## :x notesExample
to do list:

- fix hacluster
- ask IT team for feedback
- expand to prod servers


things i did:

- scrum 
- learning some sed stuff
- tested diff versions of exporter to see which one works for rhel 7
    - tested on really-cool-server-name
- changing configs so hacluster deploys successfully
    - using Puppet: adding a case depending on ver #
- added config for hacluster
    - changed job temporarily to delete hacluster for fresh restart, tmrw need to change it back to install hacluster
- realized putting k8s in vlan 3 didn’t do anything because vlans don't have east/west traffic

tomorrow:

- change back hacluster
- figure out fixing vlan traffic problem (do we need to poke holes in firewall?)

copy paste graveyard:

- [insert boring copy paste of a config file i wrote]


## :x conventional
basically, append types to your commit messages

- fix: fixed a bug
- feat: added a new feature
- more types: build, chore, ci, docs, style, refactor, test, etc
- eg: `feat: allow provided config object to extend other configs`