--
-- PostgreSQL database dump
--

-- Dumped from database version 13.18 (Debian 13.18-1.pgdg120+1)
-- Dumped by pg_dump version 13.18 (Debian 13.18-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: approved_places; Type: TABLE; Schema: public; Owner: harmony_user
--

CREATE TABLE public.approved_places (
    id integer NOT NULL,
    name character varying NOT NULL,
    location character varying NOT NULL,
    description text,
    website_url character varying
);


ALTER TABLE public.approved_places OWNER TO harmony_user;

--
-- Name: approved_places_id_seq; Type: SEQUENCE; Schema: public; Owner: harmony_user
--

CREATE SEQUENCE public.approved_places_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.approved_places_id_seq OWNER TO harmony_user;

--
-- Name: approved_places_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: harmony_user
--

ALTER SEQUENCE public.approved_places_id_seq OWNED BY public.approved_places.id;


--
-- Name: employees; Type: TABLE; Schema: public; Owner: harmony_user
--

CREATE TABLE public.employees (
    id integer NOT NULL,
    full_name character varying,
    email character varying,
    phone_number character varying,
    department character varying,
    role character varying,
    date_of_birth date,
    age integer,
    image_url character varying
);


ALTER TABLE public.employees OWNER TO harmony_user;

--
-- Name: employees_id_seq; Type: SEQUENCE; Schema: public; Owner: harmony_user
--

CREATE SEQUENCE public.employees_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.employees_id_seq OWNER TO harmony_user;

--
-- Name: employees_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: harmony_user
--

ALTER SEQUENCE public.employees_id_seq OWNED BY public.employees.id;


--
-- Name: events; Type: TABLE; Schema: public; Owner: harmony_user
--

CREATE TABLE public.events (
    id integer NOT NULL,
    name character varying,
    date date NOT NULL,
    location character varying,
    organizer character varying
);


ALTER TABLE public.events OWNER TO harmony_user;

--
-- Name: events_id_seq; Type: SEQUENCE; Schema: public; Owner: harmony_user
--

CREATE SEQUENCE public.events_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.events_id_seq OWNER TO harmony_user;

--
-- Name: events_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: harmony_user
--

ALTER SEQUENCE public.events_id_seq OWNED BY public.events.id;


--
-- Name: formation_events; Type: TABLE; Schema: public; Owner: harmony_user
--

CREATE TABLE public.formation_events (
    id integer NOT NULL,
    name character varying NOT NULL,
    date date NOT NULL,
    location character varying,
    organizer character varying,
    description text,
    type character varying NOT NULL,
    images text
);


ALTER TABLE public.formation_events OWNER TO harmony_user;

--
-- Name: formation_events_id_seq; Type: SEQUENCE; Schema: public; Owner: harmony_user
--

CREATE SEQUENCE public.formation_events_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.formation_events_id_seq OWNER TO harmony_user;

--
-- Name: formation_events_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: harmony_user
--

ALTER SEQUENCE public.formation_events_id_seq OWNED BY public.formation_events.id;


--
-- Name: potential_recruits; Type: TABLE; Schema: public; Owner: harmony_user
--

CREATE TABLE public.potential_recruits (
    id integer NOT NULL,
    first_name character varying(100) NOT NULL,
    last_name character varying(100) NOT NULL,
    phone_number character varying(15) NOT NULL,
    email character varying(100) NOT NULL,
    date_of_birth date NOT NULL,
    age integer NOT NULL,
    role_description text,
    description text,
    resume_path character varying(255)
);


ALTER TABLE public.potential_recruits OWNER TO harmony_user;

--
-- Name: potential_recruits_id_seq; Type: SEQUENCE; Schema: public; Owner: harmony_user
--

CREATE SEQUENCE public.potential_recruits_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.potential_recruits_id_seq OWNER TO harmony_user;

--
-- Name: potential_recruits_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: harmony_user
--

ALTER SEQUENCE public.potential_recruits_id_seq OWNED BY public.potential_recruits.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: harmony_user
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying NOT NULL,
    password character varying NOT NULL,
    role character varying,
    company character varying
);


ALTER TABLE public.users OWNER TO harmony_user;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: harmony_user
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO harmony_user;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: harmony_user
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: approved_places id; Type: DEFAULT; Schema: public; Owner: harmony_user
--

ALTER TABLE ONLY public.approved_places ALTER COLUMN id SET DEFAULT nextval('public.approved_places_id_seq'::regclass);


--
-- Name: employees id; Type: DEFAULT; Schema: public; Owner: harmony_user
--

ALTER TABLE ONLY public.employees ALTER COLUMN id SET DEFAULT nextval('public.employees_id_seq'::regclass);


--
-- Name: events id; Type: DEFAULT; Schema: public; Owner: harmony_user
--

ALTER TABLE ONLY public.events ALTER COLUMN id SET DEFAULT nextval('public.events_id_seq'::regclass);


--
-- Name: formation_events id; Type: DEFAULT; Schema: public; Owner: harmony_user
--

ALTER TABLE ONLY public.formation_events ALTER COLUMN id SET DEFAULT nextval('public.formation_events_id_seq'::regclass);


--
-- Name: potential_recruits id; Type: DEFAULT; Schema: public; Owner: harmony_user
--

ALTER TABLE ONLY public.potential_recruits ALTER COLUMN id SET DEFAULT nextval('public.potential_recruits_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: harmony_user
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: approved_places; Type: TABLE DATA; Schema: public; Owner: harmony_user
--

COPY public.approved_places (id, name, location, description, website_url) FROM stdin;
1	plug in kareoke	Tel Aviv	kareoke bar in tel aviv that a lot of workers enjoyed previously	https://www.plugin.co.il/
2	Miki Shemo cakes	herzeliah arena mall	A master class with pastry chef Mickey Shemu...	https://www.4chef.co.il/...
3	Laser Arena Modiin	Blood of the Maccabees Modi'in 36	Laser Arena Modiin is the largest and most diverse experience complex in Israel...	https://www.israel-laser.co.il/about/
\.


--
-- Data for Name: employees; Type: TABLE DATA; Schema: public; Owner: harmony_user
--

COPY public.employees (id, full_name, email, phone_number, department, role, date_of_birth, age, image_url) FROM stdin;
1	John Doe	john.doe@example.com	0501234567	HR	Manager	2001-03-28	43	http://localhost:8000/uploads/employees_pictures/john_doe.png
2	Jane Smith	jane.smith@example.com	0509876543	R&D	Engineer	2001-02-28	33	http://localhost:8000/uploads/employees_pictures/jane_smith.png
3	ariel amar	arielamar@gmail.com	05059221648	sales	Marketing	2001-03-28	30	http://localhost:8000/uploads/employees_pictures/ariel_amar.png
4	almog amar	almogamar@gmail.com	05045151648	sales	Marketing	2003-05-20	22	http://localhost:8000/uploads/employees_pictures/almog_amar.png
25	Rachel mol	rachel@gmail.com	0504222243	R&D	Engineer	1998-04-28	33	http://localhost:8000/uploads/employees_pictures/rachel_mol.png
15	Noam Katz	noamkatz@gmail.com	0509876543	Finance	Financial Analyst	1998-04-28	32	http://localhost:8000/uploads/employees_pictures/noam_katz.png
12	Maya Ben-David	mayaben@gmail.com	0501234567	Product	Product Manager	2001-02-28	35	http://localhost:8000/uploads/employees_pictures/maya_ben_david.png
13	Aviad Schwartz	aviadschwartz@gmail.com	0548765432	Data Science	Data Analyst	1995-02-08	30	http://localhost:8000/uploads/employees_pictures/aviad_schwartz.png
14	Shira Levi	shiralevi@gmail.com	0521234567	Sales	Marketing Assistant	2000-04-20	25	http://localhost:8000/uploads/employees_pictures/shira_levi.png
16	Yael Cohen	yaelcohen@gmail.com	0541234567	Legal practice	Legal Assistant	1997-08-12	28	http://localhost:8000/uploads/employees_pictures/yael_cohen.png
17	Daniel Ben-Ari	danielbenari@gmail.com	0587654321	Design	UI/UX Designer	1973-03-18	27	http://localhost:8000/uploads/employees_pictures/daniel_ben_ari.png
23	dor ashkenazi	doras@gmail.com	0586968321	Design	UI/UX Designer	1973-03-18	26	http://localhost:8000/uploads/employees_pictures/dor_ashkenazi.png
5	assaf amar malka	assafamarm@gmail.com	05059016875	Legal practice	lawyer	1990-05-20	35	http://localhost:8000/uploads/employees_pictures/assaf_amar_malka.png
6	eviatar kadosh	eviatarkadosh@gmail.com	0529998887	Legal practice	lawyer	1988-05-20	37	http://localhost:8000/uploads/employees_pictures/eviatar_kadosh.png
7	tomer kadosh	tomerka@gmail.com	05059018105	Legal practice	lawyer	1990-05-20	37	http://localhost:8000/uploads/employees_pictures/tomer_kadosh.png
8	meshi kadosh	meshika@gmail.com	05058816875	Interior design	Interior design	1995-06-20	30	http://localhost:8000/uploads/employees_pictures/meshi_kadosh.png
9	Yossi martziano	yossimar@gmail.com	05059048975	Logistics	Logistics Manager	1988-05-20	37	http://localhost:8000/uploads/employees_pictures/yossi_martziano.png
10	Dana Cohen	danacohen@gmail.com	0543216543	Human Resources	HR Manager	1985-11-10	39	http://localhost:8000/uploads/employees_pictures/dana_cohen.png
11	Ronen Levi	ronenlevi@gmail.com	0529876543	IT	Software Engineer	1992-03-25	33	http://localhost:8000/uploads/employees_pictures/ronen_levi.png
18	Michal Cohen	michalcohen@gmail.com	0545678901	Project Management	Project Manager	1982-05-05	43	http://localhost:8000/uploads/employees_pictures/michal_cohen.png
19	tahel kadosh	tahel@gmail.com	0504350543	R&D	Engineer	1990-09-15	33	http://localhost:8000/uploads/employees_pictures/tahel_kadosh.png
20	luna klement	luna@gmail.com	05059225742	sales	Marketing	1965-05-20	72	http://localhost:8000/uploads/employees_pictures/luna_klement.png
21	tali atias	taliat@gmail.com	05024975448	IT	helpdesk	2003-05-20	22	http://localhost:8000/uploads/employees_pictures/tali_atias.png
22	danit greenberg	danitgr@gmail.com	05043316875	IT	helpdesk	1991-05-22	29	http://localhost:8000/uploads/employees_pictures/danit_greenberg.png
24	hodaya Cohen	hodayaco@gmail.com	0558678101	Project Management	Project Manager	2002-05-05	23	http://localhost:8000/uploads/employees_pictures/hodaya_cohen.png
26	lali esposito	lali@example.com	1234567890	Sales	Sales Representative	1990-02-15	33	http://localhost:8000/uploads/employees_pictures/lali_esposito.png
27	peter lansani	peter@example.com	9876543210	Marketing	Marketing Manager	1985-02-28	38	http://localhost:8000/uploads/employees_pictures/peter_lansani.png
28	Miley Cyrus	miley@example.com	981112210	Marketing	Marketing Manager	1995-02-28	28	http://localhost:8000/uploads/employees_pictures/miley_cyrus.png
29	Michael Johnson	michaeljohnson@example.com	5551212	IT	Software Engineer	2000-03-10	23	http://localhost:8000/uploads/employees_pictures/michael_johnson.png
30	Emily Davis	emilydavis@example.com	5555555	HR	HR Specialist	1992-03-25	31	http://localhost:8000/uploads/employees_pictures/emily_davis.png
31	colleen ballinger	colleen@example.com	6526839	HR	HR Specialist	1992-03-16	31	http://localhost:8000/uploads/employees_pictures/colleen_ballinger.png
\.


--
-- Data for Name: events; Type: TABLE DATA; Schema: public; Owner: harmony_user
--

COPY public.events (id, name, date, location, organizer) FROM stdin;
1	Tom's Birthday	2025-02-06	lobby	tom
2	Late Chanukah toast	2025-03-01	Shoshi's office	hr
3	test	2025-04-01	test	test
4	Celebrate Sprint Ending!	2025-05-14	Primary Meeting Room	Sprint Leader!
5	Test Event	2025-01-15	Tel Aviv	John Doe
6	valentine's day happy hour!	2026-02-14	Open conference room in the courtyard	Liat from HR
7	purim celebration!	2025-03-14	lobby - HR	Or Dorbin
\.


--
-- Data for Name: formation_events; Type: TABLE DATA; Schema: public; Owner: harmony_user
--

COPY public.formation_events (id, name, date, location, organizer, description, type, images) FROM stdin;
1	karaoke evening for IT department	2025-01-29	plug in tel aviv	HR department	Celebrate the launch of the IT Department...	Formation	string
2	Italian Food Workshop for QA	2025-01-14	4chef herzelia	Liat simhayev	let's have fun cooking italian food together!	Formation	string
3	HR Team Building 2021	2021-06-15	Beach Resort	yossi sheli	Annual team building event	Formation	\N
4	Miris birthday from finance 2022	2022-12-21	Villa Goldis	Miri Yakobson	2022 bonding to celecrate Miris birthday	Formation	\N
5	2020 volunteer trip	2020-09-09	Volpson Hospital	Joe from marketing	Joe from marketing offered a lot of people in the company to join him in his journey to bring happiness and joy to a lot of children that are hospitalized in Volpson.	Volunteer	\N
6	Dor beach bonding trip 2023	2023-11-04	Dor beach	Noga from HR	All of the comapnys employees went to the bonding trip and enjoyes the beautiful view and a lot of fun activities!	Formation	\N
7	test	2025-05-20	test	test	test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test test v	Formation	\N
8	lazer tag for Sales department	2025-05-21	Laser Arena Modiin	HR	Unleash your inner sales warrior at Laser Arena Modiin! This high-energy team-building event will challenge your teamwork, communication, and strategic thinking. Navigate the arena's challenging maze, outmaneuver your opponents, and celebrate your victories with your team. Register now for an unforgettable experience that will boost morale and strengthen your sales force.	Formation	https://www.laser-city.co.il/wp-content/uploads/2024/08/z02.jpg
\.


--
-- Data for Name: potential_recruits; Type: TABLE DATA; Schema: public; Owner: harmony_user
--

COPY public.potential_recruits (id, first_name, last_name, phone_number, email, date_of_birth, age, role_description, description, resume_path) FROM stdin;
1	Michael	Nathan Dorbin	052-1223212	michaelnathan@gmail.com	2002-04-28	22	QA	Previously worked in software development...	\N
3	Shira	Steinbuch	053-7655678	shirast@gmail.com	1999-05-13	26	Product Manager	Worked at the company "Vardim" before its acquisition...	\N
4	Gerry	Mandelbaum	052-5381648	gerry@gmail.com	1981-03-07	54	Team Lead Developer	Over 30 years of experience in software development. Previously a product manager, improved the previous company by 17%, and sold several shares. Self-taught software development on UDEMY until becoming a team leader.	\N
5	Mila	Kunis	053-7876567	millak@gmail.com	2000-01-01	25	Head of Fun	Responsible for company bonding events in her previous role, including communication with external vendors and ensuring employee satisfaction.	\N
6	Lital	Avraham	08-7655678	litalav@gmail.com	2001-01-04	24	Helpdesk	4 years of experience in IT support at Microsoft. Completed CCNA and networking courses. Formerly a network administrator in the military.	\N
9	Hodaya	Yaakov	052-2764822	hodayaya@gmail.com	2000-06-26	25	Recruiter	Recruited employees for companies like Dell and Lenovo, hiring around 12,000 employees in 6 years. Received prior recommendations and impressive CVs sent by email.	\N
11	reef	malka	0521112221	reefmalka@gmail.com	2000-01-06	24	marketing	Results-oriented and highly motivated sales/marketing professional with a proven track record of success. Passionate about building strong client relationships and exceeding targets. Strong communication and interpersonal skills with a focus on customer satisfaction.	\N
44	shahar	hasson	0555554443	shaharh@gmail.com	2015-01-12	31	PMO	Highly motivated and results-oriented PMO with 10+ years of experience in managing and supporting complex projects across various industries. Proven ability to drive project success through effective planning, execution, and monitoring. Expertise in Agile methodologies, risk management, resource allocation, project portfolio management, tools like Jira/Asana. Seeking a challenging role in a dynamic and innovative environment.	\N
45	liran	danino	052-333999999	lirand@gmail.com	2015-01-27	28	Software Engineer	"Highly motivated and results-oriented Software Engineer with a passion for developing cutting-edge AI solutions. Proven ability to design and implement robust and scalable software systems. Eager to contribute to a dynamic and innovative team and make a significant impact on the future of AI."	\N
46	avi	toledano	0534432498	avit@gmail.com	2015-05-21	27	\N	Highly motivated and results-driven QA with a strong passion for sustainability, innovation, customer success. Proven ability to excel in. Seeking a challenging role in a collaborative environment where I can contribute to a company that makes a positive impact	\N
47	liav	bento	0529997775	liavb@gmail.com	2015-04-23	29	Senior Product Marketing Manager	Bachelor's degree in marketing, business, or a related field. 5+ years of experience in product marketing. Proven track record of successfully launching and growing products. Strong analytical skills and ability to leverage data to drive decision-making. Excellent written and verbal communication skills. Experience working in a fast-paced, dynamic environment.	\N
48	tali	simhayev	05487678521	talisi@gmail.com	2015-11-30	27	project manager	Highly motivated and results-oriented Project Manager with a proven track record of successfully delivering projects on time and within budget. Expertise in Agile methodologies, risk management, and stakeholder communication. Proven ability to lead and motivate cross-functional teams.	\N
69	sapir	heba	055-56765454	sapirhs@gmail.com	2015-10-15	22	project manager	Enthusiastic and collaborative Project Manager with a passion for driving project success. Strong communication and interpersonal skills with a proven ability to build and maintain strong relationships with stakeholders. Highly organized and detail-oriented with a focus on achieving project objectives.	\N
70	noa	kirel	0524445556	noak@gmail.com	2015-08-19	23	project manager	Results-driven Project Manager with a strong focus on delivering high-quality outcomes. Proven ability to identify and mitigate project risks, optimize resource allocation, and ensure project success. Seeking a challenging role in a dynamic and innovative environment.	\N
72	ayelet	shahar	0813547387	ayelettt@gamil.com	2025-01-06	23	fullstack developer	Studied computer science at Tal Institute in Jerusalem and graduated with honors, including Dean’s Award. 5 years of software development experience at Checkpoint.	\N
73	lital	ben yaakov	05212312343	litalbeny@gmail.com	2001-01-04	24	IT support - helpdesk	"Results-oriented Helpdesk Support Specialist with a proven track record of resolving user issues quickly and efficiently. Contributed to improving user satisfaction and reducing helpdesk ticket volume. Strong interpersonal skills and a positive attitude."	\N
75	osher	cohen	0746734563475	osherco@gmail.com	1998-09-15	27	Help Desk	"Enthusiastic and patient Helpdesk Support Specialist with a strong customer service orientation. Proven ability to effectively communicate technical information to users with varying levels of technical expertise. Eager to learn new technologies and provide exceptional support to end-users."	\N
76	shlomi	saranga	0533746533	shlomis@gmail.com	1992-02-11	33	PMO	30 years old PMO with several years of experiance in the genra.	\N
77	shay	dover	06524547859	shays@gmail.com	2000-05-24	21	Software Engineer	description fo test description fo test description fo test description fo test description fo test description fo test description fo test description fo test description fo test	\N
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: harmony_user
--

COPY public.users (id, username, password, role, company) FROM stdin;
1	harmony_user	password	test	test
2	ordo	Aa123456	system administrator	itTech
3	miriy	Aa123456	head of fun	confetti
4	test5	1	1	1
5	hanoh	1	1	1
\.


--
-- Name: approved_places_id_seq; Type: SEQUENCE SET; Schema: public; Owner: harmony_user
--

SELECT pg_catalog.setval('public.approved_places_id_seq', 4, false);


--
-- Name: employees_id_seq; Type: SEQUENCE SET; Schema: public; Owner: harmony_user
--

SELECT pg_catalog.setval('public.employees_id_seq', 32, false);


--
-- Name: events_id_seq; Type: SEQUENCE SET; Schema: public; Owner: harmony_user
--

SELECT pg_catalog.setval('public.events_id_seq', 8, false);


--
-- Name: formation_events_id_seq; Type: SEQUENCE SET; Schema: public; Owner: harmony_user
--

SELECT pg_catalog.setval('public.formation_events_id_seq', 9, false);


--
-- Name: potential_recruits_id_seq; Type: SEQUENCE SET; Schema: public; Owner: harmony_user
--

SELECT pg_catalog.setval('public.potential_recruits_id_seq', 78, false);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: harmony_user
--

SELECT pg_catalog.setval('public.users_id_seq', 5, true);


--
-- Name: approved_places approved_places_pkey; Type: CONSTRAINT; Schema: public; Owner: harmony_user
--

ALTER TABLE ONLY public.approved_places
    ADD CONSTRAINT approved_places_pkey PRIMARY KEY (id);


--
-- Name: employees employees_pkey; Type: CONSTRAINT; Schema: public; Owner: harmony_user
--

ALTER TABLE ONLY public.employees
    ADD CONSTRAINT employees_pkey PRIMARY KEY (id);


--
-- Name: events events_pkey; Type: CONSTRAINT; Schema: public; Owner: harmony_user
--

ALTER TABLE ONLY public.events
    ADD CONSTRAINT events_pkey PRIMARY KEY (id);


--
-- Name: formation_events formation_events_pkey; Type: CONSTRAINT; Schema: public; Owner: harmony_user
--

ALTER TABLE ONLY public.formation_events
    ADD CONSTRAINT formation_events_pkey PRIMARY KEY (id);


--
-- Name: potential_recruits potential_recruits_email_key; Type: CONSTRAINT; Schema: public; Owner: harmony_user
--

ALTER TABLE ONLY public.potential_recruits
    ADD CONSTRAINT potential_recruits_email_key UNIQUE (email);


--
-- Name: potential_recruits potential_recruits_pkey; Type: CONSTRAINT; Schema: public; Owner: harmony_user
--

ALTER TABLE ONLY public.potential_recruits
    ADD CONSTRAINT potential_recruits_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: harmony_user
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: ix_approved_places_id; Type: INDEX; Schema: public; Owner: harmony_user
--

CREATE INDEX ix_approved_places_id ON public.approved_places USING btree (id);


--
-- Name: ix_employees_department; Type: INDEX; Schema: public; Owner: harmony_user
--

CREATE INDEX ix_employees_department ON public.employees USING btree (department);


--
-- Name: ix_employees_email; Type: INDEX; Schema: public; Owner: harmony_user
--

CREATE UNIQUE INDEX ix_employees_email ON public.employees USING btree (email);


--
-- Name: ix_employees_full_name; Type: INDEX; Schema: public; Owner: harmony_user
--

CREATE INDEX ix_employees_full_name ON public.employees USING btree (full_name);


--
-- Name: ix_employees_id; Type: INDEX; Schema: public; Owner: harmony_user
--

CREATE INDEX ix_employees_id ON public.employees USING btree (id);


--
-- Name: ix_events_id; Type: INDEX; Schema: public; Owner: harmony_user
--

CREATE INDEX ix_events_id ON public.events USING btree (id);


--
-- Name: ix_events_name; Type: INDEX; Schema: public; Owner: harmony_user
--

CREATE INDEX ix_events_name ON public.events USING btree (name);


--
-- Name: ix_formation_events_id; Type: INDEX; Schema: public; Owner: harmony_user
--

CREATE INDEX ix_formation_events_id ON public.formation_events USING btree (id);


--
-- Name: ix_potential_recruits_id; Type: INDEX; Schema: public; Owner: harmony_user
--

CREATE INDEX ix_potential_recruits_id ON public.potential_recruits USING btree (id);


--
-- Name: ix_users_id; Type: INDEX; Schema: public; Owner: harmony_user
--

CREATE INDEX ix_users_id ON public.users USING btree (id);


--
-- Name: ix_users_username; Type: INDEX; Schema: public; Owner: harmony_user
--

CREATE UNIQUE INDEX ix_users_username ON public.users USING btree (username);


--
-- PostgreSQL database dump complete
--

