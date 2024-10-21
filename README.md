# calhacks-11


---

# Autonomous AI Society 🚁🌍

An autonomous system of AI agents performing intelligent disaster response, from analyzing distress calls, dispatching drones, finding humans in floods, and making phone calls to rescue teams. This project showcases the use of multiple agents,each responsible for a distinct role in the disaster response workflow. It integrates several advanced AI and voice technologies such as **Fetch.ai**, **Deepgram**, **Hyperbolic**, **Groq**, and **Vapi** to create an end-to-end disaster assistance system.

## 🚀 Inspiration

Disasters strike unexpectedly, and rapid response can save lives. My goal was to build an **autonomous AI-driven system** capable of managing and coordinating disaster response efforts—from analyzing distress calls to deploying drones and ensuring rescue teams reach the right location with minimal delay. This project seeks to demonstrate how AI agents can work together, making real-time decisions and coordinating disaster response, reducing human effort, and saving lives.

## 💡 What It Does

**Autonomous AI Society** consists of a network of intelligent agents, each with specific roles in disaster response:

1. **Distress Analysis Agent**: Analyzes distress calls using **Hume AI** to determine the distress level of each call and identify the city with the most urgent need for help.
2. **Drone Dispatch Agent**: Dispatches a drone to the location identified by the Distress Analysis Agent.
3. **Human Detection Agent**: Analyzes images from the drone using **Hyperbolic’s LLaMA Vision** to detect humans or animals in need of rescue. It also provides a summary of the image for rescue teams.
4. **Call Rescue Agent**: After detecting humans, this agent uses **Vapi** to place an automated call to the rescue team, providing them with a detailed description of the situation and coordinates.
5. **Drone Updates Dashboard**: Displays the results from drone analysis, including descriptions of the situation and the priority level for dispatching rescue teams.

 <img width="1440" alt="Screenshot 2024-10-20 at 11 45 00 AM" src="https://github.com/user-attachments/assets/7f98657b-1d93-4387-b13c-3ff50cc5d1f6">

## 🛠️ How I Built It

### **Technologies & Tools**
- **Fetch.ai**: Used to build the agents responsible for coordinating the disaster response system.
- **Deepgram**: Text-to-Speech and Speech-to-Text functionalities to convert the rescue instructions into voice messages, enhancing communication.
- **Hyperbolic**: Powered our human detection model using **LLaMA Vision**, which helped identify humans and potential hazards in the drone images.
- **Groq**: Used to infer the risk priority of each situation, helping the system prioritize high-risk rescue missions.
- **Vapi**: For making automated phone calls to the rescue teams, providing them with essential information about the location and the nature of the rescue operation.
- **Python & JavaScript**: Built the core system using **Python** for agent workflows and **React** for the frontend dashboards.
- **UAgents**: A library used to handle agent communications.
- **Hume AI**: Analyzed distress calls to identify the level of urgency.

### **System Architecture**

1. **Request-Sender Agent**: Initiates the process by sending incoming distress call data to the **Distress Analyzer Agent**.
   
2. **Distress Analyzer Agent**: 
   - Analyzes the distress levels of the calls using **Hume AI**.
   - Chooses the highest-priority distress call and identifies the city.
   - Dispatches the **Drone Dispatch Agent** to the identified city.

3. **Drone Dispatch Agent**: 
   - Simulates the dispatch of a drone to the identified location.
   - After dispatch, it collects images from the drone and passes them to the **Human Detection Agent**.

4. **Human Detection Agent**: 
   - Uses **Hyperbolic’s LLaMA Vision** to analyze images and detect humans or animals in need of rescue.
   - Generates a description of the scene and logs the location's coordinates.
   - Plays an audio message using **Deepgram** and sends a notification to the **Call Rescue Agent**.
   
5. **Call Rescue Agent**:
   - Receives a summary of the detected situation from the **Human Detection Agent**.
   - Makes a phone call to the rescue team using **Vapi**, providing detailed instructions based on the analysis.

6. **Frontend Dashboards**:
   - **Distress Calls Dashboard**: Displays distress calls and their severity levels.
   - **Drone Results Dashboard**: Displays analysis results of the drone images, including the descriptions and priority levels, powered by **Groq**.

## ⚠️ Challenges I Faced

- **Coordination Between Multiple Agents**: Ensuring that the agents worked in sequence and communicated effectively posed a challenge. I used **Fetch.ai**'s agent framework to create an efficient, scalable communication network.
- **Visual Data Processing**: Processing drone images in real-time with **Hyperbolic LLaMA Vision** was a complex task, requiring careful tuning to ensure accurate human detection.
- **Prioritization**: Determining the right priorities for rescue missions was critical. **Groq**'s risk analysis inference helped streamline this process.

## 🌟 Accomplishments

- Successfully deployed an **end-to-end autonomous system** that manages disaster response, from analyzing distress calls to dispatching drones, detecting humans in flooded waters and making calls to rescue teams.
- Integrated **Hyperbolic's LLaMA Vision**, **Deepgram**, and **Vapi** to create a system capable of both real-time analysis and communication.
- Built highly interactive and responsive **dashboards** that visually represent the distress and drone results.

## 📚 What I Learned

- **AI Can Save Lives**: Building this system showed us the power of AI in making real-time, life-saving decisions.
- **Agent Communication**: We learned a lot about orchestrating multiple agents using **Fetch.ai** and ensuring smooth, synchronous workflows between them.
- **The Power of Voice Technology**: Using **Deepgram** and **Vapi** helped us realize the importance of voice in critical scenarios like disaster management.

## 🔮 What’s Next

- **Live Data Integration**: Integrating real-time satellite or drone footage for continuous monitoring.
- **Scaling**: Expanding the system to handle multiple disasters across different regions simultaneously.
- **Collaborative Response**: Allow multiple drones and agents to work together in a larger-scale operation, making the entire disaster response system even more autonomous.

## 🏆 Project Sponsors

This project was made possible thanks to the following amazing technologies:
- **Fetch.ai**: For building intelligent agents and enabling seamless communication between them.
- **Deepgram**: For enabling real-time voice communications and Text-to-Speech functionalities.
- **Groq**: For providing fast risk priority inference that helps decide rescue operations.
- **Hyperbolic**: For their **LLaMA Vision**, which allowed us to detect humans in drone images.
- **Vapi**: For enabling automated phone calls to rescue teams with vital rescue information.

## 🎤 Elevator Pitch

**Autonomous AI Society** is an intelligent disaster response system powered by AI agents, capable of analyzing distress calls, dispatching drones, detecting humans in floods, and coordinating rescue efforts via phone calls to emergency teams. It streamlines disaster management, allowing for faster and more effective rescues.


