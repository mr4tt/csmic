Title: Ergo
Date: 2022-06-27 10:47am
Category: Case Studies
Tags: case-study
Slug: ergo
Authors: Mrat
Summary: Connecting people one event at a time.

**Timeframe**: March 2022 → June 2022

**Role**: UX Designer

**Tools**: Figma, Figjam

---

![cover photo]({attach}/images/ergo/cover.png "test")

### Connecting people one event at a time.

Imagine a time where you were thrilled to attend a particular event with a couple close friends. As the date nears, they suddenly cancel on you. You still want to go with someone, but you don't know if your other friends are also attending.

We created ERGO, a social event app that connects you with people on your friends list and people you may know through others. 

Features:
- Help you find events that friends are planning to attend
- Notify you when a friend arrives at an event
- Discover who your friends are going to events with
- Messaging to talk about events or attending together
- Display Map that shows nearby friends currently at particular events

## Motivation

### ERGO helps people who attend events and struggle to find others to attend with despite enjoying going with friends, especially after plans fall through.

ERGO's goal is to bring people together through social events and location-based services. When people attend large events, they may not know if their friends are attending until they are notified of their location through social media, mutual friends, or even coincidentally running into them. To solve this problem, we created an app that incorporated location-based services and notifications to simplify the process of finding friends who want to attend events.

After conducting both a literature review and a survey, our presumptions were proven to be true.
 
For the literature review, we researched how location-based services function and how many applications utilize location features. We found that location-based services are often used for recommending users about locations close to them. These user recommendations may be applied to various services, like dining, routing, and communication. As technology advances, there is a lot of room for location-based services to expand and grow.

Our surveys also provided a lot of insights. **26 out of 28** people already **use application or services that utilize user locations** for specific features. While many people tend to find location-based services useful, they are wary regarding privacy and safety concerns stemming from them. In terms of planning and attending events, 19 out of 21 participants enjoyed attending events with friends, yet **16 out of 21 agreed their plans sometimes or often fall through**. Based on this data, there is an opportunity for a social event application that helps users plan events with friends through chat and location-based functionalities. 

## Design Process

Session 1:

<div class="row">
  <div class="col col--8">
    Our design process for ERGO consisted mainly of two parts: a rough prototyping session and a refined prototyping session, conducted with the same participants. 
    
    Our team brainstormed our process through a separate Figjam file, exploring Figjam functionalities and widgets. It was challenging to determine how we would integrate social interactions within an online space, without creating am overly complex prototype. We intended to simulate a real-world situation where people would attend an event alone, and find friends or new people to meet up at the event together. To do this, we used many Figjam widgets to assist us in simulating this process. Participants would begin by first reading the instructions, then attaching their name below an event. We created a limit of 10 participants per event to create equal groups. Participants navigated to the map corresponding to their chosen event and rolled a dice to determine their role for the round. They were asked to play out these roles and use chat widgets to communicate. We repeated this process in our second round.
    <br>
  </div>
  <div class="col">
    <img src="{attach}/images/ergo/ergoGif.gif"/>
  </div>
</div>

We received a lot of honest feedback on the challenges participants faced in our first prototype. The most common criticism was that our prototype was too confusing; there were too many steps that participants had to quickly understand and do. Our overfamiliarity with the prototype hindered our ability to consider a participant's perspective on the instructions. The steps and roles were overly complex and confusing. We also integrated too many widgets without considering how these may simulate a real-life scenario. 

Furthermore, our team did not have a firm grasp on how we wanted our app to look like, so our simulation explanation to the audience was also convoluted. This meant participants did not have a clear mental model of the experience we were trying to create. All of the feedback we received was very helpful, which allowed for us to iterate and improve our prototype for the future session.

[insert session 1 pic/pdf]
Preview of our first prototyping session, conducted in Figjam.

Session 2:

Based on feedback and analysis of the interactions from our first prototype session, we made drastic changes going into our refined prototype. Before creating our refined prototype, our team took the time to solidify our concept for an app, and specifically what exactly we want to simulate for it. Each team member discussed their idea of the app, and how they see a potential situation arising from it. After solidifying our concept, we mainly pivoted from multiple event maps to simple locations within a singular event. To simulate real-world situations, we created a Figma prototype that consisted of various situations and texts with two choices. Based on a participant's choices, they would be directed to a particular Figjam link, which represented a different room based on the scenario they selected. Participants were instructed to do 2 steps once they were in the Figjam. They had to use a group chat to meet up with weaker-tied friends, and decide where they wanted to meet up together. Upon deciding, they could take a picture of themselves or use a star stamp to mark their meet-up location. 

Our second prototyping session went smoothly and was not overly complex. Participants noted that they understood what was being simulated and enjoyed the prototype overall. 
We made major improvements from our previous prototyping session. The Figma scenarios were good at simulating real-world choices regarding whether to hang out with friends at a concert. In the Figjams, there were a couple of minor issues. One of the particular Figjam rooms was much more populated than the remaining 3. This made it a bit more difficult for some participants to chat, as some were more hesitant in smaller groups. [something something represents irl] Additionally, there was a slight issue with our initial idea for chatting. Initially,  our team wanted to use a pre-set comment, in which participants could freely chat and reply there without any issues of participants simultaneously typing. Overall, our second prototyping session went very well.

[second prototyping] Preview of one section of our second prototyping session. It was done in both Figma and multiple Figjams.

## Final Prototype

<div class="col">
  <div class="row">
    <div class="col col--3">
        <figure>
            <img src="{attach}/images/ergo/screen1.png">
            <figcaption>
                <p> 
                    Home Screen: 
                    <br>
                    Users can view upcoming events nearby and plan and book events Within these user's events, they can view other friends who are also attending. 
                </p>
            </figcaption>
        </figure>
    </div>
    <div class="col col--3">
        <figure>
            <img src="{attach}/images/ergo/screen2.png">
            <figcaption>
                <p> 
                    Friend Activity: 
                    <br>
                    Users can see the events their friends are at or planning to attend. Users can view their strong ties, but also weak ties (friends-of-friends).
                </p>
            </figcaption>
        </figure>
    </div>
    <div class="col col--3">
        <figure>
            <img src="{attach}/images/ergo/screen3.png">
            <figcaption>
                <p> 
                    Notifications: 
                    <br>
                    Users can see their notifications, such as event updates, where ERGO will notify a user about their friends planning events or someone's arrival at an event. 
                </p>
            </figcaption>
        </figure>
    </div>
  </div>
  <div class="row">
    <div class="col col--3">
        <figure>
            <img src="{attach}/images/ergo/screen4.png">
            <figcaption>
                <p> 
                    Private Messages: 
                    <br>
                    Users can see their messages to people and the locations of friends you that you have recently just chatted with (if enabled). 
                </p>
            </figcaption>
        </figure>
    </div>
    <div class="col col--3">
        <figure>
            <img src="{attach}/images/ergo/screen5.png">
            <figcaption>
                <p> 
                    Group Chats: 
                    <br>
                    People can chat in groups created by mutual friends. This is a great way to connect weak ties based on mutual strong tied friends. 
                </p>
            </figcaption>
        </figure>
    </div>
    <div class="col col--3">
        <figure>
            <img src="{attach}/images/ergo/screen6.png">
            <figcaption>
                <p> 
                    Friends Nearby:
                    <br>
                    The map displays the nearby locations of friends when they are currently at an event. This helps users locate one another at the same event.
                </p>
            </figcaption>
        </figure>
    </div>
  </div>
</div>


## Social Structures and Complexities

Through experiences and our team's research, we know finding common interests amongst people in the same social circles has been done before. These are features that are almost expected from social media apps, such as a friends list, liking and subscribing to artists, an explore page of artists and their upcoming events. Liking and sharing posts are also common amongst social media apps. In some applications, social tie strength can be measured through the use of these features. The more activity that one person does within the app that includes other users increases their tie strength.

Now the issue is about users who do not like interacting with apps as much. One way to tell about a weak tie strength is based around the lack of interactivity within the app. However, we can't establish if the real reason that users have weak tie strength either because they do not have the same amount of interest with some people over others, or if those users have a cognitive load that does not allow them to use social media apps at the same rate as those with stronger social ties. There's a possibility that the tie strength is weak is more due to this lack of cognitive load than the lack of interests that two mutually known users 

The mix of friends list and in person events will naturally lead mutual friends to be in the same vicinity of each other. By creating that small spark that leads towards them knowing of each other's presence within an event, it leads to a more natural meet up than purposefully going out of your way and taking up cognitive resources to establish communication through manually going through the process of wanting to find others to meet up.

## Contributions

Thank you to my teammates: Danel Sullivan, Iisha Kshatriya, Keith Lim, and Sergio Ramirez.

### Conducting Research & Pitching Ideas

**Crystal**, **Danel**, and **Iisha** conducted a literature search on our early concept, which was generally around the topic of location-based services. They each searched for around 3-5 articles and papers to research. Each discussed and wrote down critical information about location-based services. **Keith** and **Sergio** created the user survey and organized the questions to be asked. They worked on also analyzing the results from our survey. **All 5 team members** sent out the survey to collect over 20 responses, as well as pitching ideas. We divided up both the survey data gathering and pitch ideas into 4 per teammate, so each team member collected 4 survey response and also pitched 4 preliminary ideas. 

### Prototyping Sessions

**Crystal**, **Danel**, **Keith**, and **Sergio** discussed the process and worked on each of the prototyping sessions. We established collaboration through weekly meetings. The four of us worked together to create our prototype and the instructions corresponding to it. We reviewed our feedback and interactions in both sessions, and iterated from our first prototyping session to make changes and improvements moving into our second prototyping session. 

### Final Prototype & Portfolio

**Crystal**, **Danel**, **Keith**, and **Sergio** worked on the final prototype. We worked together to decide on how the final prototype will look and the specific features we want in it. **Danel** and **Sergio** both worked on sections of our team portfolio. Each of our **5 team members** all contributed to the final slides, and recorded their assigned sections.

### Final Presentation
https://youtu.be/Upzj-sL4XVU

<!-- <figure class="float-left">
    <img src="{attach}/images/ergo/ergoGif.gif">
    <figcaption> <p> testing </p> </figcaption>
</figure>

 aaaaaaa
<br> -->