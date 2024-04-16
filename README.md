# I4C Controlled Vocabulary (CV) for use in archiving ESD output

This is a fork of the [CORDEX-CMIP6 CV](https://github.com/WCRP-CORDEX/cordex-cmip6-cv) to develop a new CV for RCM-emulator output data to be used in Impetus4Change.

You can check differences with the base CORDEX-CMIP6 CV for dynamical downscaling [here](https://github.com/impetus4change/cordex-cmip6-cv/compare/main..esd).

## ESD method registration
To register your institution or ESD method, please submit an issue using these forms:

* [New institution_id](https://github.com/impetus4change/cordex-cmip6-cv/issues/new?assignees=&labels=Register+institution-id&projects=&template=institution_id.yaml&title=institution_id+registration+of+...)
* [New source_id (i.e. model)](https://github.com/impetus4change/cordex-cmip6-cv/issues/new?assignees=&labels=Register+source-id&projects=&template=source_id.yaml&title=source_id+registration+of+...)

These forms will automatically create a pull request, where further details can be discussed.
Models must not be distinguished by the `institution_id`.
Do not register a new `source_id` if the same model or method configuration is already registered by other institution.
Just request to add your `institution_id` to the list of the corresponding `source_id`.

To request changes in any other CV use a [blank issue](https://github.com/impetus4change/cordex-cmip6-cv/issues/new) with a meaningful title.
E.g. `source_type: add YOURNEWTYPE` or `source_id: update MODEL123A further_info_url`

To view current repository contents in HTML format, point your browser to:

| target | URL |
| :-- | :-- |
| `institution_id` | [CORDEX-CMIP6_institution_id.html](https://impetus4change.github.io/cordex-cmip6-cv/CORDEX-CMIP6_institution_id.html) |
| `source_id` | [CORDEX-CMIP6_source_id.html](https://impetus4change.github.io/cordex-cmip6-cv/CORDEX-CMIP6_source_id.html) |

The CVs build on logic that is described in [Deliverable 3.4: Description of the Data Reference syntax for archiving results of statistical and emulation-based downscaling]() and the [CORDEX-CMIP6 Archiving Specifications for Dynamical Downscaling](https://doi.org/10.5281/zenodo.10961068) documents.
