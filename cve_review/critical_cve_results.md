# Critical Vulnerabilities Report

## CVE-2025-0207

**Description:** A critical vulnerability has been found in code-projects Online Shoe Store 1.0. The issue affects the file `/function/login.php`, where manipulation of the `password` argument leads to SQL injection. The attack can be launched remotely, and the exploit has been publicly disclosed.

**CVSS v3.1 Score:** 9.8 (Critical)
**Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H

**Affected Product:** code-projects Online Shoe Store 1.0

**Weaknesses:** 
- CWE-74
- CWE-89

**References:**
- [Product Information](https://code-projects.org/)
- [Exploit Details](https://gist.github.com/th4s1s/d10dfaebae75c8dbe54ad83d63725d81)
- [VulDB Entry](https://vuldb.com/?id.290144)

---

## CVE-2025-0208

**Description:** A critical vulnerability was found in code-projects Online Shoe Store 1.0, affecting an unknown part of the file `/summary.php`. The manipulation of the `tid` argument leads to SQL injection. The attack can be initiated remotely, and the exploit has been publicly disclosed.

**CVSS v3.1 Score:** 9.8 (Critical)
**Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H

**Affected Product:** code-projects Online Shoe Store 1.0

**Weaknesses:** 
- CWE-74
- CWE-89

**References:**
- [Product Information](https://code-projects.org/)
- [Exploit Details](https://gist.github.com/th4s1s/24925a20d1f9336858dee1cbbb30c249)
- [VulDB Entry](https://vuldb.com/?id.290145)

---

## CVE-2025-0210

**Description:** A critical vulnerability has been found in Campcodes School Faculty Scheduling System 1.0. The vulnerability affects an unknown functionality of the file `/admin/ajax.php?action=login`, where manipulation of the `username` argument leads to SQL injection. The attack can be launched remotely, and the exploit has been publicly disclosed.

**CVSS v3.1 Score:** 9.8 (Critical)
**Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H

**Affected Product:** Campcodes School Faculty Scheduling System 1.0

**Weaknesses:** 
- CWE-74
- CWE-89

**References:**
- [Exploit Details](https://github.com/shaturo1337/POCs/blob/main/Blind%20SQL%20Injection%20in%20School%20Faculty%20Scheduling%20System.md)
- [VulDB Entry](https://vuldb.com/?id.290155)
- [Product Website](https://www.campcodes.com/)

---

## CVE-2025-0211

**Description:** A critical vulnerability was found in Campcodes School Faculty Scheduling System 1.0. The issue affects some unknown functionality of the file `/admin/index.php`, where manipulation of the `page` argument leads to file inclusion. The attack may be launched remotely, and the exploit has been publicly disclosed.

**CVSS v3.1 Score:** 9.8 (Critical)
**Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H

**Affected Product:** Campcodes School Faculty Scheduling System 1.0

**Weaknesses:** 
- CWE-73

**References:**
- [Exploit Details](https://github.com/shaturo1337/POCs/blob/main/LFI%20in%20School%20Faculty%20Scheduling%20System.md)
- [VulDB Entry](https://vuldb.com/?id.290156)
- [Product Website](https://www.campcodes.com/)

---

## CVE-2025-0212

**Description:** A critical vulnerability was found in Campcodes Student Grading System 1.0. This affects an unknown part of the file `/view_students.php`. The manipulation of the `id` argument leads to SQL injection. It is possible to initiate the attack remotely, and the exploit has been publicly disclosed.

**CVSS v3.1 Score:** 9.8 (Critical)
**Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H

**Affected Product:** Campcodes Student Grading System 1.0

**Weaknesses:** 
- CWE-74
- CWE-89

**References:**
- [Exploit Details](https://github.com/shaturo1337/POCs/blob/main/SQL%20Injection%20in%20Student%20Grading%20System.md)
- [VulDB Entry](https://vuldb.com/?id.290157)
- [Product Website](https://www.campcodes.com/)

---

## CVE-2025-0213

**Description:** A critical vulnerability was found in Campcodes Project Management System 1.0. This vulnerability affects unknown code of the file `/forms/update_forms.php?action=change_pic2&id=4`. The manipulation of the `file` argument leads to unrestricted upload. The attack can be initiated remotely, and the exploit has been publicly disclosed.

**CVSS v3.1 Score:** 9.8 (Critical)
**Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H

**Affected Product:** Campcodes Project Management System 1.0

**Weaknesses:** 
- CWE-284
- CWE-434

**References:**
- [Exploit Details](https://github.com/shaturo1337/POCs/blob/main/Remote%20Code%20Execution%20via%20Arbitrary%20File%20Upload%20in%20Project%20Management%20System.md)
- [VulDB Entry](https://vuldb.com/?id.290158)
- [Product Website](https://www.campcodes.com/)

---

## CVE-2024-13136

**Description:** A critical vulnerability was found in wangl1989 mysiteforme 1.0. Affected by this issue is the function `rememberMeManager` of the file `src/main/java/com/mysiteforme/admin/config/ShiroConfig.java`. The manipulation leads to deserialization. The attack may be launched remotely, and the exploit has been publicly disclosed.

**CVSS v3.1 Score:** 9.8 (Critical)
**Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H

**Affected Product:** wangl1989 mysiteforme 1.0

**Weaknesses:** 
- CWE-502

**References:**
- [GitHub Issue](https://github.com/wangl1989/mysiteforme/issues/52)
- [VulDB Entry](https://vuldb.com/?id.290210)

---

## CVE-2025-0229

**Description:** A critical vulnerability has been found in code-projects Travel Management System 1.0. This issue affects some unknown processing of the file `/enquiry.php`. The manipulation of the argument `pid/t1/t2/t3/t4/t5/t6/t7` leads to SQL injection. The attack may be initiated remotely, and the exploit has been publicly disclosed.

**CVSS v3.1 Score:** 9.8 (Critical)
**Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H

**Affected Product:** code-projects Travel Management System 1.0

**Weaknesses:** 
- CWE-74
- CWE-89

**References:**
- [Exploit Details](https://github.com/Huandtx/cve/blob/main/cve/sql1.md)
- [VulDB Entry](https://vuldb.com/?id.290225)
- [Product Website](https://code-projects.org/)

---

## CVE-2025-0230

**Description:** A critical vulnerability was found in code-projects Responsive Hotel Site 1.0. Affected is an unknown function of the file `/admin/print.php`. The manipulation of the `pid` argument leads to SQL injection. It is possible to launch the attack remotely, and the exploit has been publicly disclosed.

**CVSS v3.1 Score:** 9.8 (Critical)
**Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H

**Affected Product:** code-projects Responsive Hotel Site 1.0

**Weaknesses:** 
- CWE-74
- CWE-89

**References:**
- [Exploit Details](https://github.com/Huandtx/cve/blob/main/cve/Responsive%20Hotel%20Site/sql1.md)
- [VulDB Entry](https://vuldb.com/?id.290226)
- [Product Website](https://code-projects.org/)

---

## CVE-2025-0233

**Description:** A critical vulnerability was found in Codezips Project Management System 1.0. This affects an unknown part of the file `/pages/forms/course.php`. The manipulation of the `course_name` argument leads to SQL injection. It is possible to initiate the attack remotely, and the exploit has been publicly disclosed.

**CVSS v3.1 Score:** 9.8 (Critical)
**Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H

**Affected Product:** Codezips Project Management System 1.0

**Weaknesses:** 
- CWE-74
- CWE-89

**References:**
- [GitHub Issue](https://github.com/1074923869/CVE/issues/1)
- [VulDB Entry](https://vuldb.com/?id.290229)

---

## CVE-2024-12402

**Description:** The Themes Coder – Create Android & iOS Apps For Your Woocommerce Site plugin for WordPress is vulnerable to privilege escalation via account takeover in all versions up to, and including, 1.3.4. This is due to the plugin not properly validating a user's identity prior to updating their password through the `update_user_profile()` function. This makes it possible for unauthenticated attackers to change arbitrary user's passwords, including administrators, and leverage that to gain access to their account.

**CVSS v3.1 Score:** 9.8 (Critical)
**Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H

**Affected Product:** Themes Coder – Create Android & iOS Apps For Your Woocommerce Site WordPress plugin (versions up to 1.3.4)

**Weaknesses:** 
- CWE-288

**References:**
- [Plugin Source Code](https://plugins.trac.wordpress.org/browser/tc-ecommerce/trunk/controller/app_user.php#L338)
- [Wordfence Vulnerability Report](https://www.wordfence.com/threat-intel/vulnerabilities/id/1ec14b1e-6d1a-4451-9fce-ac064623d92f?source=cve)

---

## CVE-2024-12252

**Description:** The SEO LAT Auto Post plugin for WordPress is vulnerable to file overwrite due to a missing capability check on the `remote_update` AJAX action in all versions up to, and including, 2.2.1. This makes it possible for unauthenticated attackers to overwrite the `seo-beginner-auto-post.php` file which can be leveraged to achieve remote code execution.

**CVSS v3.1 Score:** 9.8 (Critical)
**Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H

**Affected Product:** SEO LAT Auto Post WordPress plugin (versions up to 2.2.1)

**Weaknesses:** 
- CWE-94

**References:**
- [WordPress Plugin Page](https://wordpress.org/plugins/seo-beginner-auto-post/)
- [Wordfence Vulnerability Report](https://www.wordfence.com/threat-intel/vulnerabilities/id/67df10cc-ce3c-4157-9860-7e367062f710?source=cve)

---

## CVE-2024-12264

**Description:** The PayU CommercePro Plugin plugin for WordPress is vulnerable to privilege escalation in all versions up to, and including, 3.8.3. This is due to `/wp-json/payu/v1/generate-user-token` and `/wp-json/payu/v1/get-shipping-cost` REST API endpoints not properly verifying a user's identity prior to setting the users ID and auth cookies. This makes it possible for unauthenticated attackers to create new administrative user accounts.

**CVSS v3.1 Score:** 9.8 (Critical)
**Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H

**Affected Product:** PayU CommercePro Plugin for WordPress (versions up to 3.8.3)

**Weaknesses:** 
- CWE-287

**References:**
- [Plugin Source Code](https://plugins.trac.wordpress.org/browser/payu-india/tags/3.8.3/includes/class-payu-shipping-tax-api-calculation.php#L187)
- [Wordfence Vulnerability Report](https://www.wordfence.com/threat-intel/vulnerabilities/id/bf037e4a-2dd7-4296-b86b-635901d2d68f?source=cve)

---

## CVE-2024-12470

**Description:** The School Management System – SakolaWP plugin for WordPress is vulnerable to privilege escalation in all versions up to, and including, 1.0.8. This is due to the registration function not properly limiting what roles a user can register as. This makes it possible for unauthenticated attackers to register as an administrative user.

**CVSS v3.1 Score:** 9.8 (Critical)
**Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H

**Affected Product:** School Management System – SakolaWP WordPress plugin (versions up to 1.0.8)

**Weaknesses:** 
- CWE-266

**References:**
- [WordPress Plugin Page](https://wordpress.org/plugins/sakolawp-lite/)
- [Wordfence Vulnerability Report](https://www.wordfence.com/threat-intel/vulnerabilities/id/db1c581b-5cc9-46c0-ba5d-605642697729?source=cve)

---

## CVE-2024-11642

**Description:** The Post Grid Master – Custom Post Types, Taxonomies & Ajax Filter Everything with Infinite Scroll, Load More, Pagination & Shortcode Builder plugin for WordPress is vulnerable to Local File Inclusion in all versions up to, and including, 3.4.12 via the 'locate_template' function. This makes it possible for unauthenticated attackers to include and execute arbitrary files on the server, allowing the execution of any