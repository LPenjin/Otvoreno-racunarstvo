--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2
-- Dumped by pg_dump version 13.2

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
-- Name: clan; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.clan (
    datumuclanjenja date NOT NULL,
    sifra_plave character(5) NOT NULL,
    imeprezime character(100) NOT NULL,
    imanarancastu boolean NOT NULL,
    pocasnoclanstvo boolean NOT NULL,
    clanstvovrijedido date NOT NULL
);


ALTER TABLE public.clan OWNER TO postgres;

--
-- Name: jediouprave; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jediouprave (
    pozicija character(20) NOT NULL,
    sifra_plave character(5) NOT NULL,
    godina integer NOT NULL
);


ALTER TABLE public.jediouprave OWNER TO postgres;

--
-- Name: sekcija; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sekcija (
    ime character(20) NOT NULL,
    pocetaksastanka character(10) NOT NULL,
    prostor character(20) NOT NULL,
    sef character(5) NOT NULL
);


ALTER TABLE public.sekcija OWNER TO postgres;

--
-- Name: uclanjen_u; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.uclanjen_u (
    sifra_plave character(5) NOT NULL,
    ime character(20) NOT NULL
);


ALTER TABLE public.uclanjen_u OWNER TO postgres;

--
-- Name: uprava; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.uprava (
    godina integer NOT NULL,
    pocetaksastanka character(10) NOT NULL
);


ALTER TABLE public.uprava OWNER TO postgres;

--
-- Data for Name: clan; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.clan (datumuclanjenja, sifra_plave, imeprezime, imanarancastu, pocasnoclanstvo, clanstvovrijedido) FROM stdin;
2022-10-01	AA-20	Pero Peric                                                                                          	f	f	2023-10-01
2022-10-01	AA-21	Ana Anic                                                                                            	f	f	2023-10-01
2022-10-01	AA-22	Fran Franic                                                                                         	f	f	2023-10-01
2022-10-01	AA-23	Luka Lukic                                                                                          	f	f	2023-10-01
2022-10-01	AA-24	Toni Tonic                                                                                          	f	f	2023-10-01
2022-10-01	AA-25	Klara Klaric                                                                                        	f	f	2023-10-01
2022-10-01	AA-26	Bartol Bartolic                                                                                     	f	f	2023-10-01
2022-10-01	AA-27	Zaga Zagic                                                                                          	f	f	2023-10-01
2022-10-01	AA-28	Karla Karlic                                                                                        	f	f	2023-10-01
2022-10-01	AA-29	Drago Dragic                                                                                        	f	f	2023-10-01
2022-10-01	AA-30	Koka Kokic                                                                                          	f	f	2023-10-01
2022-10-01	AA-31	Alex Turner                                                                                         	f	f	2023-10-01
2022-10-01	AA-32	Andro Andric                                                                                        	f	f	2023-10-01
2022-10-01	AA-33	Antonio Antonic                                                                                     	f	f	2023-10-01
2022-10-01	AA-35	Ivan Ivic                                                                                           	f	f	2023-10-01
2022-10-01	AA-36	Disko Čiča                                                                                          	f	f	2023-10-01
2022-10-01	AA-37	Sef Sefic                                                                                           	t	f	2023-10-01
2022-10-01	AA-38	Stevo Blagajnik                                                                                     	t	f	2023-10-01
2022-10-01	AA-39	Marko Tajnik                                                                                        	t	f	2023-10-01
2022-10-01	AA-40	Marko Markic                                                                                        	t	f	2023-10-01
2022-10-01	AA-41	Josip Josipovic                                                                                     	t	f	2023-10-01
2022-10-01	AA-42	Nikola Nikolic                                                                                      	t	f	2023-10-01
2022-10-01	AA-43	Marin Marinic                                                                                       	t	f	2023-10-01
2022-10-01	AA-44	Patrik Patrikic                                                                                     	t	f	2023-10-01
2022-10-01	AA-45	Juraj Juric                                                                                         	t	f	2023-10-01
2022-10-01	AA-46	Helena Helenic                                                                                      	t	f	2023-10-01
2022-10-01	AA-47	Arnold Schwarzenger                                                                                 	t	f	2023-10-01
2022-10-01	AA-48	Silvester Stalone                                                                                   	t	f	2023-10-01
2022-10-01	AA-49	Paolo Paolic                                                                                        	t	f	2023-10-01
2022-10-01	AA-50	Tamara Tamaric                                                                                      	t	f	2023-10-01
\.


--
-- Data for Name: jediouprave; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jediouprave (pozicija, sifra_plave, godina) FROM stdin;
Sef                 	AA-37	2022
Blagajnik           	AA-38	2022
Tajnik              	AA-39	2022
\.


--
-- Data for Name: sekcija; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sekcija (ime, pocetaksastanka, prostor, sef) FROM stdin;
Bike sekcija        	18:00     	Tech prostor        	AA-35
Disko sekcija       	18:00     	Kabina              	AA-24
Foto sekcija        	18:00     	Foto prostorija     	AA-50
Comp sekcija        	18:00     	Comp Prostorija     	AA-41
Video sekcija       	18:00     	Video Prostorija    	AA-44
Tech sekcija        	18:00     	Tech Prostorija     	AA-43
Glazbena sekcija    	18:00     	Glazbena prostorija 	AA-48
Planinarska sekcija 	18:00     	Tech prostorija     	AA-46
Dramska sekcija     	18:00     	Ispod stepenica     	AA-42
\.


--
-- Data for Name: uclanjen_u; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.uclanjen_u (sifra_plave, ime) FROM stdin;
AA-20	Bike sekcija        
AA-35	Bike sekcija        
AA-24	Disko sekcija       
AA-42	Dramska sekcija     
AA-50	Foto sekcija        
AA-48	Glazbena sekcija    
AA-48	Planinarska sekcija 
AA-41	Comp sekcija        
AA-44	Video sekcija       
AA-43	Tech sekcija        
AA-21	Disko sekcija       
AA-20	Disko sekcija       
AA-22	Disko sekcija       
AA-23	Disko sekcija       
AA-25	Disko sekcija       
AA-26	Disko sekcija       
AA-27	Tech sekcija        
AA-28	Tech sekcija        
AA-29	Tech sekcija        
AA-30	Tech sekcija        
AA-31	Video sekcija       
AA-33	Video sekcija       
AA-36	Bike sekcija        
AA-37	Bike sekcija        
AA-38	Bike sekcija        
AA-39	Dramska sekcija     
AA-40	Comp sekcija        
AA-42	Comp sekcija        
AA-45	Comp sekcija        
AA-46	Comp sekcija        
AA-47	Comp sekcija        
AA-49	Comp sekcija        
AA-46	Planinarska sekcija 
\.


--
-- Data for Name: uprava; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.uprava (godina, pocetaksastanka) FROM stdin;
2022	19:00     
\.


--
-- Name: clan clan_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.clan
    ADD CONSTRAINT clan_pkey PRIMARY KEY (sifra_plave);


--
-- Name: jediouprave jediouprave_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jediouprave
    ADD CONSTRAINT jediouprave_pkey PRIMARY KEY (sifra_plave, godina);


--
-- Name: sekcija sekcija_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sekcija
    ADD CONSTRAINT sekcija_pkey PRIMARY KEY (ime);


--
-- Name: uclanjen_u uclanjen_u_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.uclanjen_u
    ADD CONSTRAINT uclanjen_u_pkey PRIMARY KEY (sifra_plave, ime);


--
-- Name: uprava uprava_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.uprava
    ADD CONSTRAINT uprava_pkey PRIMARY KEY (godina);


--
-- Name: jediouprave jediouprave_godina_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jediouprave
    ADD CONSTRAINT jediouprave_godina_fkey FOREIGN KEY (godina) REFERENCES public.uprava(godina);


--
-- Name: jediouprave jediouprave_sifra_plave_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jediouprave
    ADD CONSTRAINT jediouprave_sifra_plave_fkey FOREIGN KEY (sifra_plave) REFERENCES public.clan(sifra_plave);


--
-- Name: sekcija sekcija_sef_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sekcija
    ADD CONSTRAINT sekcija_sef_fkey FOREIGN KEY (sef) REFERENCES public.clan(sifra_plave);


--
-- Name: uclanjen_u uclanjen_u_ime_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.uclanjen_u
    ADD CONSTRAINT uclanjen_u_ime_fkey FOREIGN KEY (ime) REFERENCES public.sekcija(ime);


--
-- Name: uclanjen_u uclanjen_u_sifra_plave_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.uclanjen_u
    ADD CONSTRAINT uclanjen_u_sifra_plave_fkey FOREIGN KEY (sifra_plave) REFERENCES public.clan(sifra_plave);


--
-- PostgreSQL database dump complete
--

