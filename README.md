# Registry claim audit

An offline static audit compares documentation claims about CAS Registry Number string judgement with Python source call evidence. It does not execute inspected code or access the network. The check digit judges shape and checksum, not registry membership or substance properties.

Install from a local distribution with `python3 -m pip install PATH`. Run:

```text
casrn-validation-claim-audit audit [repo] [--json] [--verbose] [--fail-on high|medium] [--ignore PREFIX]
python3 -m casrn_validation_claim_audit audit [repo]
casrn-validation-claim-audit --version
```

The default repository is the current directory. Repeated ignore options exclude path prefixes. Findings at the threshold exit 2, a clean result exits 0, and usage or I/O errors exit 1. The default threshold is high; medium includes test-only evidence. JSON output contains a findings array. The identifiers are:

```text
documented-casrn-validation-claim-false
documented-no-casrn-validation-claim-false
```

Root README and Markdown under docs are scanned outside fenced blocks; inline code counts. Matching ignores case, hyphen differences and whitespace. Negative spans are removed before positive matching. Python files are parsed statically; production and test evidence are separate, while fixtures, docs, examples and symlinks are excluded. Syntax errors produce no evidence. Aliased imports are resolved and locally shadowed names are excluded. Generic named attribute calls and imported named calls count; library-specific calls must resolve to the supported module.

## Differentiation

This audit does not cover generic input validation.
This audit does not cover ISBN-10 and ISBN-13 book numbers.
This audit does not cover ISSN serial numbers.
This audit does not cover IBAN bank accounts.
This audit does not cover UUID identifiers.
This audit does not cover semantic versions.
This audit does not cover MAC hardware addresses.
This audit does not cover BIC bank identifiers.
This audit does not cover cron expression validation.
This audit does not cover cron expression description.
This audit does not cover scheduled execution.
This audit does not cover calendar date validation.
This audit does not cover call timeouts.
This audit does not cover payment processing.
This audit does not cover credit card extraction.
This audit does not cover account authentication with a code or link.
This audit does not cover password hash verification.
This audit does not cover password hashing.
This audit does not cover password generation.
This audit does not cover PDF encryption.
This audit does not cover sending email.
This audit does not cover sending SMS.
This audit does not cover document extraction.
This audit does not cover barcode decoding from images.
This audit does not cover email address validation.
This audit does not cover phone number validation.
This audit does not cover password strength.
This audit does not cover JSON Schema validation.
This audit does not cover credit card number validation.
This audit does not cover domain validation.
This audit does not cover URL validation.
This audit does not cover IP address validation.
This audit does not cover JSON parsing.
This audit does not cover regex matching.
This audit does not cover URL parsing.
This audit does not cover fetching web addresses.
This audit does not cover DNS resolution.
This audit does not cover account barcode generation.
This audit does not cover account number extraction.
This audit does not cover vehicle number extraction.
This audit does not cover vehicle number decoding.
This audit does not cover vehicle history lookup.
This audit does not cover hex colour validation.
This audit does not cover ORCID identifiers.
This audit does not cover ISNI identifiers.
This audit does not cover DOI validation or resolution.
This audit does not cover CUSIP identifiers.
This audit does not cover SEDOL identifiers.
This audit does not cover ISIN identifiers.
This audit does not cover security record lookup.
This audit does not cover security identifier extraction.
This audit does not cover IMEI identifiers.
This audit does not cover MEID identifiers.
This audit does not cover ESN identifiers.
This audit does not cover ISMN identifiers.
This audit does not cover ISAN identifiers.
This audit does not cover GRid identifiers.
This audit does not cover EAN identifiers.
This audit does not cover generic serial numbers.
This audit does not cover FIGI identifiers.
This audit does not cover financial instrument lookup.
This audit does not cover financial instrument extraction.
This audit does not cover ISRC recording codes.
This audit does not cover Ethereum addresses.
This audit does not cover Binance Smart Chain addresses.
This audit does not cover Tron addresses.
This audit does not cover Litecoin addresses.
This audit does not cover Dogecoin addresses.
This audit does not cover bitcoin addresses.
This audit does not cover transaction hashes.
This audit does not cover private keys.
This audit does not cover block explorer lookups.
This audit does not cover address generation.
This audit does not cover address extraction.
This audit does not cover payment receipt confirmation.
This audit does not cover spreadsheet reading.
This audit does not cover spreadsheet generation.
This audit does not cover word document reading.
This audit does not cover word document generation.
This audit does not cover presentation reading.
This audit does not cover presentation generation.
This audit does not cover PDF extraction.
This audit does not cover PDF generation.
This audit does not cover PDF merging.
This audit does not cover PDF splitting.
This audit does not cover PDF rotation.
This audit does not cover PDF form filling.
This audit does not cover PDF watermarking.
This audit does not cover PDF redaction.
This audit does not cover PDF compression.
This audit does not cover PDF annotation.
This audit does not cover table extraction.
This audit does not cover OCR.
This audit does not cover e-signatures.
This audit does not cover screen recording.
This audit does not cover video generation.
This audit does not cover QR code generation.
This audit does not cover barcode generation.
This audit does not cover barcode scanning.
This audit does not cover audio mixing.
This audit does not cover audio generation.
This audit does not cover audio editing.
This audit does not cover audio source separation.
This audit does not cover speech recognition.
This audit does not cover text-to-speech.
This audit does not cover noise suppression.
This audit does not cover music generation.
This audit does not cover music transcription.
This audit does not cover InChI identifiers.
This audit does not cover SMILES notation.
This audit does not cover EC numbers.
This audit does not cover UN transport numbers.
This audit does not cover PubChem compound lookup.
This audit does not cover chemical structure validation.
This audit does not cover other chemical identifiers.

## Limitations

```text
validate cas number
```

This matched wording may describe a manual ordering step.

```text
cas number validation
```

This matched wording may describe a roadmap feature.

```text
cas number validator
```

This matched wording may refer to a hosted page.

```text
cas number check
```

This matched wording may refer to a field-presence lint rule.

```text
check cas number
```

This matched wording may describe a manual runbook step.

```text
verify cas number
```

This matched wording may describe visual confirmation of substance identity.

```text
cas number verification
```

This matched wording may refer to an external service result.

```text
validate cas rn
```

This matched wording may describe a manual runbook step.

```text
cas rn validation
```

This matched wording may name a specification section without implementation.

```text
valid cas number
```

This matched wording may be example output.

```text
cas number is valid
```

This matched wording may be example output.

```text
cas number is invalid
```

This matched wording may be example error text.

```text
cas number validity
```

This matched wording may name a configuration flag or column.

```text
cas number format validation
```

This matched wording may describe a format without code.

```text
validate cas registry number
```

This matched wording may describe a manual runbook step.

```text
cas registry number validation
```

This matched wording may name a specification section without implementation.

```text
cas rn check
```

This matched wording may name a lab checklist item.

```text
check cas rn
```

This matched wording may describe a manual runbook step.

```text
verify cas rn
```

This matched wording may describe visual confirmation of substance identity.

```text
validate cas number format
```

This matched wording may describe a format without code.

```text
cas
```

This excluded wording is ambiguous by itself.

```text
cas number
```

This excluded wording only names an identifier.

```text
cas registry number
```

This excluded wording only names an identifier.

```text
cas rn
```

This excluded wording only names an abbreviation.

```text
registry number
```

This excluded wording can refer to any registry.

```text
validate cas
```

This excluded wording can refer to something else.

```text
check digit
```

This excluded wording only names a checksum.

```text
chemical identifier
```

This excluded wording can refer to other identifiers.

A compact call only reformats input.

A check-digit calculation alone does not judge a complete number.

A regular expression alone is not evidence.

A length check alone is not evidence.

A hyphen-position check alone is not evidence.

A digit-only check alone is not evidence.

A registry lookup alone is not evidence.

Generating a registry number is not evidence.

An InChI judgement is not evidence.

A SMILES judgement is not evidence.

An EC-number judgement is not evidence.

A UN-number judgement is not evidence.

A PubChem lookup is not evidence.

A chemical-structure judgement is not evidence.

The checksum misses some single-digit typos: 14-17-5 passes despite being a mistyped 64-17-5.

The supported library compacts bare digits, accepting 50000 as 50-00-0.

The library does not establish registry membership.

The library does not establish substance properties.

The validators package has no corresponding route for cross-checking.

Static call fingerprints cannot establish runtime behavior.
