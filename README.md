# Green_QR_code_or_e-pass
Information going into the pass:
  * Status of the person i.e, whether he/she is corona +ve or corona -ve or considered to be in quarantine.
  * Age of the person
  * Unique Id of the person
  * Name
  * Gender
 Pass issued by a competent authority like government.
 
 Security requirements to be ensured :
  *  Authenticating the pass i.e it is not a duplicate one by seeing the photo on company Id.
 
 For changing the status of a suspicious case by the labs Kerberos will be used to ensure that the information is updated by approved labs.
 
 By sending the information to the central server. Securing the information to be sent and receive using Diffie-Hellman or Elgamal Cryptosystem.
 
 A central server is needed which gives status of the person. Updating the information is done through a different server.
 This server will access information hold by the latter server.
 
 Date and time of the test is important with the date and time of issue of the pass. This is checked during verification.
 
 Given cryptosystem are used to ensure the security.
 
 Confidentiality, authentication,integrity and non-repudiation is relevant.
 
 Concerns are to ensure that the Ids are not forged as a person can use another person QR id. For this watermark is considered to be used.

QR code is verified using Image analysis module or some other modules by uploading it manually on the web site.
