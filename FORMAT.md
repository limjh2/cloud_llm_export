# Export Collection Format

## Placement

Each complete provider delivery is one export set:

```text
exports/<provider>/YYYY-MM-DD/
```

The provider name is lowercase and stable; the date is the provider delivery
or export date. Everything below the set directory preserves the delivered
layout.

## Immutability

Never edit, rename internally, extract over, deduplicate, or delete files in an
accepted set. A correction or newer delivery is a new dated set.

## Export catalog

`EXPORTS.tsv` columns:

```text
provider  export_date  relative_path  file_count  size_bytes  notes
```

## File manifest

`FILE_MANIFEST.tsv` columns:

```text
relative_path  size_bytes  sha256
```

Both TSVs remain header-only in the public template. Filled rows, file paths,
hashes, and notes exist only in a private local instance.
