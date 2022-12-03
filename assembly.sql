--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5 (Homebrew)
-- Dumped by pg_dump version 14.5 (Homebrew)

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
-- Name: construction; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.construction (
    id text NOT NULL,
    name character varying(32) NOT NULL,
    description character varying(200) NOT NULL,
    syntax character varying(200) NOT NULL,
    example text NOT NULL
);


ALTER TABLE public.construction OWNER TO postgres;

--
-- Name: datatype; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.datatype (
    id text NOT NULL,
    name character varying(32) NOT NULL,
    description character varying(200) NOT NULL,
    example text NOT NULL
);


ALTER TABLE public.datatype OWNER TO postgres;

--
-- Name: function; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.function (
    id text NOT NULL,
    name character varying(32) NOT NULL,
    description character varying(200) NOT NULL,
    params character varying(255)[] NOT NULL,
    return_type_id text NOT NULL,
    example text NOT NULL,
    note character varying(100) NOT NULL
);


ALTER TABLE public.function OWNER TO postgres;

--
-- Name: glossary; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.glossary (
    id text NOT NULL,
    name character varying(32) NOT NULL,
    description character varying(200) NOT NULL
);


ALTER TABLE public.glossary OWNER TO postgres;

--
-- Name: library; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.library (
    id text NOT NULL,
    name character varying(50),
    type character varying(32) NOT NULL,
    description character varying(200) NOT NULL,
    repo_link character varying(50) NOT NULL
);


ALTER TABLE public.library OWNER TO postgres;

--
-- Name: operator; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.operator (
    id text NOT NULL,
    name character varying(32) NOT NULL,
    syntax character varying(200) NOT NULL,
    example text NOT NULL
);


ALTER TABLE public.operator OWNER TO postgres;

--
-- Data for Name: construction; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.construction (id, name, description, syntax, example) FROM stdin;
122fb9bd-f9ae-4b1b-9013-37cea41e3210	The data Sectio	Розділ даних використовується для оголошення ініціалізованих даних або констант. Ці дані не змінюються під час виконання.	section.data	section.data msg db 'Hello, world!', 0xa  ;string to be printed len equ $ - msg;length of the string
00d94240-cbfe-4ebc-9ebd-52f0470a7703	The bss Section	Розділ bss використовується для оголошення змінних.	section.bss	section .bss variable: resb 4
35e27cc1-c41b-4477-bda7-185623de9c38	The text section	Текстовий розділ використовується для зберігання фактичного коду. Цей розділ повинен починатися з оголошення global _start, яке повідомляє ядру, де починається виконання програми.	section.text	section.text  global _start _start:
9df5ced7-f94a-4b03-aee0-6fdca2ceaea5	Програма Привіт Світ	Наступний код мови асемблера відображає на екрані рядок «Hello World».	msg db 'Hello, world!', 0xa  ;string to be printed	section\t.text    global _start     ;must be declared for linker (ld)_start:\t            ;tells linker entry point    mov\tedx,len     ;message length   mov\tecx,msg     ;message to write   mov\tebx,1       ;file descriptor (stdout)   mov\teax,4       ;system call number (sys_write)   int\t0x80        ;call kernel   mov\teax,1       ;system call number (sys_exit)   int\t0x80        ;call kernel   section\t.data msg db 'Hello, world!', 0xa  ;string to be printedlen equ $ - msg     ;length of the string
\.


--
-- Data for Name: datatype; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.datatype (id, name, description, example) FROM stdin;
b883adb1-810a-442c-befe-065eacea668a	BYTE	8-розрядне ціле число без знаку	
f4797d65-b901-45f0-a29d-a63c32b427b1	SBYTE	8-розрядне ціле число зі знаком	
b3fc316c-65df-42ec-9761-8e89d7e2c051	WORD	16-бітове ціле число без знаку	
17983aad-8ed4-4f18-ac8c-57a24d63517e	SWORD	16-розрядне ціле число зі знаком	
2580dcc0-2562-4917-aeda-d806c88748c4	DWORD	32-розрядне ціле число без знаку	
0ebda57a-86d0-4df5-9762-44018b8e9712	SDWORD	32-розрядне ціле число зі знаком	
33959906-b734-4f46-80ea-3af0f078a830	FWORD	48-бітове ціле число	
22d725bc-445f-41c0-99fb-60912f7d7d34	QWORD	64-бітове ціле число	
bae8e620-7bca-47d1-8667-10c0f431100e	TBYTE	80 біт (10 байт) ціле число	
4937cc29-a7b5-4d50-88a8-fda17ea18e7f	REAL4	32 біт (4 байти) короткий реальний	
3423f9a5-e701-465a-8a04-efd03abeaa6f	REAL8	64 біт (8 байти) короткий реальний	
d793e30d-f4da-4723-8483-9ad62cff687a	REAL10	80 біт (10 байти) короткий реальний	
\.


--
-- Data for Name: function; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.function (id, name, description, params, return_type_id, example, note) FROM stdin;
9f056925-1296-49ad-ab64-1b2edc4d5af8	assuming NASM x86	Функція NASM налаштує свій стековий кадр і візьме параметри зі стеку для використання у функції. Значення зберігається в EAX.	{num1,num2}	f4797d65-b901-45f0-a29d-a63c32b427b1	func:\n    xor eax, eax\n    mov eax, 10\n    add eax, 5\n    ret ;// essentially identical to: pop [register] -> jmp [register]\n\n\n_start:\n    call func\n    mov ebx, eax ;// Address of this instruction is pushed onto the stack\n    ;// ebx is now 15	Використовуйте call для виклику функції та ret для повернення з функції.
\.


--
-- Data for Name: glossary; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.glossary (id, name, description) FROM stdin;
c3368f25-c013-4a25-8c38-418c5371c648	AB	Assembly Bill
2f76612c-e4ea-4893-b2db-987662ee4da9	B & F	Committee on Banking and Finance
5fa6d9a0-d5da-4977-a6eb-5bc27c855f68	Macro	Макрос мови асемблера — це шаблонний формат черевика, який представляє ряд або шаблон операторів
00341060-4294-47b1-bd13-a684ea993e20	Оператори	Оператори, які також називаються командами, є логічними виразами, які з’являються після поля мітки.
34bc7e35-a8dd-47f6-817e-35b3fd497962	Мітка	Мітка — це символ, який представляє адресу, де зберігається інструкція або дані. Його призначення — діяти як адресат, коли на нього посилаються у заяві.
\.


--
-- Data for Name: library; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.library (id, name, type, description, repo_link) FROM stdin;
af535c8c-6e12-4912-9de3-bfcdcdaebb50	BearSSL	Basic	BearSSL static libraries compiled for x86 and x64 assembler	https://github.com/mrfearless/libraries/
ea7b7bff-7396-419a-a8dd-605636c1028d	cJSON - cjson	Basic	cjson v1.7.12 static libraries compiled for x86 and x64 assembler	https://github.com/master/cJSON
0a5a1a48-c0ef-4de3-8292-9b06182bc55b	cJSON - cjson	Basic	cjson v1.7.12 static libraries compiled for x86 and x64 assembler	https://github.com/master/cJSON
98c637c2-de94-40e4-b1ee-f18805ec9263	cJSON - cjson	Compiling	cjson v1.7.12 static libraries compiled for x86 and x64 assembler	https://github.com/master/cJSON
5d6c1929-6046-4c39-9d96-b00a55be1ae0	SQLite	Database	SQLite static libraries compiled for x86 and x64 assembler	https://github.com/mrfearles/master/SQLite
\.


--
-- Data for Name: operator; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.operator (id, name, syntax, example) FROM stdin;
158c88f8-473a-4d49-aa5e-8a293f263396	Збільште змінну пам'яті COUNT	INC COUNT	
f0755ced-fb22-478b-929f-2861e2f5124d	MOV TOTAL	MOV TOTAL, 50	Перенесіть значення 48 у змінну пам'яті TOTAL: MOV TOTAL, 48
37ff3f7f-3f90-4007-ad5e-fb70d7d81095	 Додати до реєстру	ADD AH, BH	Додайте вміст реєстру BH до реєстру AH: ADD AH, BH
846440d0-de92-4415-8dcc-f98c91ab314b	 Операція над змінною	AND MASK1, 128	Виконайте операцію І над змінними MASK1 і 128: AND MASK1, 128
d92554a1-66c2-4743-8a30-fb85d9f3074a	 Операція додавання	ADD MARKS, 10	Додайте 10 до змінної MARKS: ADD MARKS, 10
211d0467-58c2-49ab-8ba9-ae79b3c77a76	 Перенесення значення	MOV AL, 10	Перенесіть значення 10 в регістр AL: MOV AL, 10
\.


--
-- Name: construction construction_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.construction
    ADD CONSTRAINT construction_pkey PRIMARY KEY (id);


--
-- Name: datatype datatype_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.datatype
    ADD CONSTRAINT datatype_pkey PRIMARY KEY (id);


--
-- Name: function function_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.function
    ADD CONSTRAINT function_pkey PRIMARY KEY (id);


--
-- Name: glossary glossary_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.glossary
    ADD CONSTRAINT glossary_pkey PRIMARY KEY (id);


--
-- Name: library library_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.library
    ADD CONSTRAINT library_pkey PRIMARY KEY (id);


--
-- Name: operator operator_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.operator
    ADD CONSTRAINT operator_pkey PRIMARY KEY (id);


--
-- Name: function_params; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX function_params ON public.function USING gin (params);


--
-- Name: function_return_type_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX function_return_type_id ON public.function USING btree (return_type_id);


--
-- Name: function function_return_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.function
    ADD CONSTRAINT function_return_type_id_fkey FOREIGN KEY (return_type_id) REFERENCES public.datatype(id);


--
-- PostgreSQL database dump complete
--

