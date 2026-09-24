import re

with open('d:/3D ELEMENTS/100-3d-web-elements/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the head and styles
head_replacement = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>3D Web Elements - Gallery</title>
    <meta name="description" content="Sophisticated interactive component library.">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles/design-system.css">
    <style>
        body {
            font-family: var(--font-sans);
            background-color: var(--bg-primary);
            color: var(--text-primary);
            margin: 0;
            padding: 0;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }

        .gallery-header {
            text-align: center;
            padding: var(--space-16) var(--space-4) var(--space-8);
            max-width: 800px;
            margin: 0 auto;
        }

        .gallery-header h1 {
            font-size: var(--text-4xl);
            font-weight: 800;
            letter-spacing: -0.02em;
            margin-bottom: var(--space-4);
            color: var(--text-primary);
        }

        .gallery-header p {
            font-size: var(--text-lg);
            color: var(--text-secondary);
            font-weight: 400;
            line-height: 1.6;
        }

        .gallery-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(450px, 1fr));
            gap: var(--space-8);
            max-width: 1800px;
            margin: 0 auto;
            padding: var(--space-4) var(--space-6) var(--space-16);
        }

        .component-stage {
            background-color: var(--bg-secondary);
            border-radius: var(--radius-xl);
            overflow: hidden;
            display: flex;
            flex-direction: column;
            border: 1px solid var(--border-subtle);
            transition: border-color var(--time-base) var(--ease-out);
        }

        .component-stage:hover {
            border-color: var(--border-strong);
        }

        .stage-header {
            padding: var(--space-4) var(--space-6);
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--border-subtle);
            background-color: var(--bg-elevated);
        }

        .stage-title {
            font-size: var(--text-base);
            font-weight: 500;
            color: var(--text-primary);
        }

        .badge {
            font-size: var(--text-xs);
            padding: var(--space-1) var(--space-3);
            border-radius: var(--radius-full);
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        /* Generic badge styling to catch all previous ones */
        [class*="badge-"] { background: var(--surface-interactive); color: var(--accent-base); }
        .badge-webgl, .badge-shader { color: var(--info); }
        .badge-css, .badge-scroll { color: var(--success); }
        .badge-drag, .badge-click { color: var(--warning); }

        .stage-preview {
            height: 500px;
            position: relative;
            background-color: var(--bg-primary);
        }

        .stage-preview iframe {
            width: 100%;
            height: 100%;
            border: none;
            display: block;
        }

        .section-divider {
            text-align: center;
            padding: var(--space-16) var(--space-4) var(--space-8);
            color: var(--text-muted);
            font-size: var(--text-sm);
            letter-spacing: 0.2em;
            text-transform: uppercase;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: var(--space-4);
        }

        .section-divider::before,
        .section-divider::after {
            content: "";
            height: 1px;
            width: 60px;
            background-color: var(--border-subtle);
        }

        @media (max-width: 768px) {
            .gallery-grid {
                grid-template-columns: 1fr;
                gap: var(--space-6);
            }
            .stage-preview {
                height: 400px;
            }
        }
    </style>
</head>
<body>
    <header class="gallery-header">
        <h1>Interaction Laboratory</h1>
        <p>A sophisticated collection of original, interactive components exploring motion, space, and material.</p>
    </header>'''

# Replace from <!DOCTYPE html> down to <header class="header"> (and its contents)
new_content = re.sub(r'<!DOCTYPE html>.*?</header>', head_replacement, content, flags=re.DOTALL)

# Replace class names to match new design
new_content = new_content.replace('class="grid"', 'class="gallery-grid"')
new_content = new_content.replace('<article class="card">', '<article class="component-stage">')
new_content = new_content.replace('<article class="card xl">', '<article class="component-stage xl">')
new_content = new_content.replace('class="card-header"', 'class="stage-header"')
new_content = new_content.replace('class="card-title"', 'class="stage-title"')
new_content = new_content.replace('class="demo-area"', 'class="stage-preview"')

with open('d:/3D ELEMENTS/100-3d-web-elements/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Updated index.html')
