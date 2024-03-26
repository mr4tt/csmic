Title: Ergo
Date: 2022-06-27 10:47am
Category: Portfolio
Tags: case-study
Slug: ergo
Imgfolder: ergo
opengraph_image: cover.png
Summary: Connecting people one event at a time.
status: hidden

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

Our surveys also provided a lot of insights. **26 out of 28** people already **use application or services that utilize user locations** for specific features. While many people tend to find location-based services useful, they are wary regarding privacy and safety concerns stemming from them. In terms of planning and attending events, 19 out of 21 participants enjoyed attending events with friends, yet **16 out of 21 agreed their plans sometimes or often fall through**. 

Based on this data, we saw an opportunity for a social event application that helps users plan events with friends through chat and location-based functionalities. 

## Design Process

Our design process for ERGO consisted of two parts: 

- A rough prototyping session (Session 1)
- A refined prototyping session, conducted with the same participants (Sesson 2)
  
### Session 1:

#### Prototype Design

<div class="row">
  <div class="col col--8">
    We brainstormed the process with Figjam, exploring Figjam functionalities and widgets. It was challenging to decide how to integrate social interactions in an online space without creating an overly complex prototype. 
    We wanted to simulate the real-world experience of someone attending an event without any prior plans, then finding friends at the event. 
    <br><br>
    To accomplish this, we used many Figjam widgets to try mimicking different ways people communicate in real life. 
    <br><br>
    The first prototype's steps: 
    <ul> 
        <li> Read the instructions </li>
        <li> Attach your name to the event you'd like to attend </li>
        <li> Navigate to the map of your chosen event </li>
        <li> Roll a dice (Figma widget) to determine their role for the round (such as raver or friendless) </li>
        <li> Act out role with others around you, using chat widgets </li>
    </ul>
    
    We ran two rounds of scenarios so people would get multiple roles to play. 

    <br>
  </div>
  <div class="col">
    <img src="{attach}/images/ergo/ergoGif.gif"/>
  </div>
</div>

#### Results

We received a lot of honest feedback on the challenges participants faced in our first prototype. The most common criticism was that our prototype was too confusing; there were too many steps that participants had to quickly understand and do. Our overfamiliarity with the prototype hindered our ability to consider a participant's perspective on the instructions. The steps and roles were also complex and confusing. We integrated too many widgets, and people had trouble keeping track of everything. 

Furthermore, our team did not have a firm grasp on how we wanted our app to look like, so our simulation explanation to the audience was also convoluted. This meant participants did not have a clear mental model of the experience we were trying to create. All of the feedback we received was very helpful, which allowed for us to iterate and improve our prototype for the future session.

[note: video has actual stats n stuff lol]

[insert session 1 pic/pdf]
Preview of our first prototyping session, conducted in Figjam.

### Session 2:

#### Prototype Design

Based on feedback and analysis of the interactions from our first prototype session, we made drastic changes going into our refined prototype. Before creating our refined prototype, we solidified app concept. Each team member discussed their app ideas and what situations in real life it would apply in. After solidifying our concept, we pivoted from multiple event maps to simple locations within a singular event. To simulate real-world situations, we created a Figma prototype with various situations and texts with two choices. Based on a participant's choices, they would be directed to a particular Figjam link, which represented a different room based on the scenario they selected. Once in the Figjam, participants were to: 

- Use a group chat to meet up with weaker-tied friends, and decide where they wanted to meet up together
- Mark their preferred meet-up location. 

#### Results

Our second prototyping session went smoothly and was not overly complex due to major improvements from our previous prototyping session. Participants noted that they understood what was being simulated and enjoyed the prototype overall. 

The Figma scenarios were better at simulating real-world choices regarding whether to hang out with friends at a concert. However, the Figjams had a couple of minor issues. One of the Figjam rooms was much more populated than the other three. This made it a bit more difficult for some participants to chat, as some were more hesitant in smaller groups. [something something represents irl] Additionally, there was a slight issue with our initial idea for chatting. Initially,  our team wanted to use a pre-set comment, in which participants could freely chat and reply there without any issues of participants simultaneously typing. Overall, our second prototyping session went very well.

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

Through experiences and our team's research, we know finding common interests amongst people in the same social circles are expected features in many social media apps. These include features like a friends list, liking and subscribing to artists, an explore page of artists and their upcoming events. Liking and sharing posts are also common amongst social media apps. In some applications, social tie strength can be measured through the use of these features. The more activity that one person does within the app that includes other users increases their tie strength.

Now the issue is about users who do not like interacting with apps as much. One way to tell about a weak tie strength is based around the lack of interactivity within the app. However, we can't establish if the real reason that users have weak tie strength either because they do not have the same amount of interest with some people over others, or if those users have a cognitive load that does not allow them to use social media apps at the same rate as those with stronger social ties. There's a possibility that the tie strength is weak is more due to this lack of cognitive load than the lack of interests that two mutually known users. 

The mix of friends list and in person events will naturally lead mutual friends to be in the same vicinity of each other. By creating that small spark that leads towards them knowing of each other's presence within an event, it leads to a natural meet up rather than forcing yourself to go out of your way to meet new people.

## Next Steps

stuff

Thank you to my teammates: Danel Sullivan, Iisha Kshatriya, Keith Lim, and Sergio Ramirez.

My contributions:

- Conducted part of the literature search on location based services
- Pitched preliminary ideas based on survey data
- Created prototype and further iterations
- Designed final prototype
- Worked on final presentation slides

### Final Presentation

[https://youtu.be/Upzj-sL4XVU](https://youtu.be/Upzj-sL4XVU)

<!-- <figure class="float-left">
    <img src="{attach}/images/ergo/ergoGif.gif">
    <figcaption> <p> testing </p> </figcaption>
</figure>

 aaaaaaa
<br> -->