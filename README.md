<h1 align="center">Hi there 👋, I'm Logan</h1>

<h3><em>Research Coordinator @ <a href="https://poldracklab.org/">Poldrack Lab</a>, Stanford University</em></h3>

- 🌱 learning `.go`
- ⚙️ use daily: `.js`, `.html`, `.css`, `.py`
- ⚡️ passionate about `reproducibility`, `open-source science`, `naturalistic neuroimaging`
  
---

### 💭 About me 

<details>
  <summary><strong>TS interfaces</strong></summary>

  
  ```typescript
  interface Job {
  employer: string;
  department: string;
  mentors: string[];
}

interface Seeking {
  actively: boolean;
  ofInterest: string[];
}

interface Interests {
  research: string[];
  seeking: Seeking;
  communities: string[];
}

interface Education {
  degree: string;
  institution: string;
  year: number;
  honors: string;
}

interface Me {
  code: string[];
  tools: string[];
  research: string[];
  job: Job;
  interests: Interests;
  hobbies: string[];
  education: Education;
}
  ```
</details>

```typescript
const Logan: Me = {
  code: ["JavaScript", "TypeScript", "HTML", "CSS", "Python"],
  tools: ["Tailwind CSS", "React", "Node", "Next.js", "Styled-Components", "Docker", "Singularity"],
  research: ["fMRI", "EEG", "open-source", "reproducibility", "cognitive tasks"],
  job: {
    employer: "Stanford University",
    department: "Psychology",
    mentors: ["Patrick Bissett", "Russell Poldrack"],
  },
  interests: {
    research: ["software for science", "cognitive neuroscience", "neuroimaging"],
    seeking: {
      actively: false,
      ofInterest: ["PhD", "Software Engineer", "Data Engineer"]
    },
    communities: ["US-RSE", "Stanford Data Science", "OpenSource@Stanford"]
  },
  hobbies: ["biking", "hiking", "volleyball"],
  education: {
      degree: "BSc in Neuroscience",
      institution: "Temple University",
      year: 2023,
      honors: "Summa Cum Laude"
  }
};
```
